''' OONI '''
import csv
import gzip
import io
from collections import Counter
from os import path
from pprint import pprint
from threading import Thread

import arrow
import boto3
import click
import orjson as json
from boto3.s3.transfer import TransferConfig
from botocore import UNSIGNED
from botocore.config import Config


class OONIS3:
    ''' OONI S3 bucket '''

    def __init__(self) -> None:
        self.s3client = boto3.client('s3', config=Config(
            region_name='eu-central-1',
            user_agent='OCF.tw OONI-Research github.com/ocftw/ooni-research',
            signature_version=UNSIGNED,
            connect_timeout=120,
            read_timeout=120,
        ))

    def list_webconnectivity(self, date='20231110', hour='09', location='TW'):
        ''' List objects '''
        return self.s3client.list_objects_v2(
            Bucket='ooni-data-eu-fra',
            Prefix=f'raw/{date}/{hour}/{location.upper()}/webconnectivity/',
            Delimiter='/',
        )


def count_asn(date, loc, oonis3=None):
    ''' Count ASN '''
    if oonis3 is None:
        oonis3 = OONIS3()

    result = {'counts': {}, 'network_type': {}}

    s3_object = oonis3.list_webconnectivity(
        date=date.format('YYYYMMDD'),
        hour=date.format('HH'),
        location=loc,
    )

    pprint(s3_object)

    if 'Contents' not in s3_object:
        return result

    for file_info in s3_object['Contents']:
        if not file_info['Key'].endswith('jsonl.gz'):
            continue

        print(file_info['Key'])
        with io.BytesIO() as file_obj:
            oonis3.s3client.download_fileobj(Key=file_info['Key'],
                                             Bucket='ooni-data-eu-fra',
                                             Fileobj=file_obj,
                                             Config=TransferConfig())

            with gzip.GzipFile(fileobj=io.BytesIO(file_obj.getvalue())) as raw_data:
                for raw in raw_data:
                    json_data = json.loads(raw)
                    if json_data['probe_asn'] not in result['counts']:
                        result['counts'][json_data['probe_asn']] = 0

                    result['counts'][json_data['probe_asn']] += 1

                    if 'network_type' in json_data['annotations']:
                        if json_data['annotations']['network_type'] not in result['network_type']:
                            result['network_type'][json_data['annotations']
                                                   ['network_type']] = 0

                        result['network_type'][json_data['annotations']
                                               ['network_type']] += 1

    return result


def asn_count_container(container, serios, *args, **kwargs):
    ''' with save container '''
    container[serios] = count_asn(*args, **kwargs)


def span_date():
    ''' Span date '''
    for date in arrow.Arrow.span_range('hour',
                                       arrow.Arrow.utcnow().shift(hours=-10).datetime,
                                       arrow.Arrow.utcnow().datetime):
        print(date)
        print(date[0].format('YYYYMMDD'))
        print(date[0].format('HH'))


@click.group()
def cli():
    ''' cli for groups '''


@cli.command('lookback', short_help='lookback datas by frame')
@click.option('--units', default=36, help='lookback by frame')
@click.option('--loc', default='TW', help='location')
@click.option('--frame', default='hours', help='location')
def lookback(units=36, loc='TW', frame='hour'):
    ''' lookback the datas '''
    oonis3 = OONIS3()
    result_total = {'counts': Counter(), 'network_type': Counter()}
    with open(f'./lookback_{loc}_{arrow.Arrow.utcnow().format("YYYYMMDD")}_{units}_{frame}.csv',
              'w+', encoding='UTF8') as csv_files:
        csv_write = csv.DictWriter(
            csv_files,
            fieldnames=('loc', 'date', 'hour', 'statistics'),
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_write.writeheader()
        periods = list(arrow.Arrow.span_range('hour',
                                              arrow.Arrow.utcnow().shift(
                                                  **{frame: units*-1}).datetime,
                                              arrow.Arrow.utcnow().datetime,
                                              exact=True))[:-1]
        chunks = [periods[n:n+5] for n in range(0, len(periods), 5)]

        for dates in chunks:
            gathers = []
            results = [None] * 5
            for num, date in enumerate(dates):
                gathers.append(Thread(target=asn_count_container, kwargs={
                    'container': results, 'serios': num,
                    'date': date[0], 'loc': loc, 'oonis3': oonis3}))

            for gather in gathers:
                gather.start()

            for gather in gathers:
                gather.join()

            for num, date in enumerate(dates):
                csv_write.writerow({'date': date[0].format('YYYY/MM/DD'),
                                    'hour': date[0].format('HH'),
                                    'statistics': json.dumps(results[num]),
                                    'loc': loc,
                                    })

                result_total['counts'].update(results[num]['counts'])
                result_total['network_type'].update(
                    results[num]['network_type'])

    pprint(dict(result_total))


@cli.command('span', short_help='Period of datas')
@click.option('--start', help='start date, YYYY/MM/DD')
@click.option('--end', help='end date, YYYY/MM/DD')
@click.option('--loc', default='TW', help='location')
def span(start, end, loc='TW'):
    ''' Period of datas '''
    oonis3 = OONIS3()
    result_total = {'counts': Counter(), 'network_type': Counter()}

    with open(f'./span_{loc}_{arrow.get(start).format("YYYYMMDD")}_{arrow.get(end).format("YYYYMMDD")}.csv',
              'w+', encoding='UTF8') as csv_files:
        csv_write = csv.DictWriter(
            csv_files,
            fieldnames=('loc', 'date', 'hour', 'statistics'),
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_write.writeheader()
        periods = list(arrow.Arrow.span_range('hour',
                                              arrow.get(start).datetime,
                                              arrow.get(end).datetime,
                                              exact=True))
        chunk_nums = 40
        chunks = [periods[n:n+chunk_nums]
                  for n in range(0, len(periods), chunk_nums)]

        for dates in chunks:
            gathers = []
            results = [None] * chunk_nums
            for num, date in enumerate(dates):
                gathers.append(Thread(target=asn_count_container, kwargs={
                    'container': results, 'serios': num,
                    'date': date[0], 'loc': loc, 'oonis3': oonis3}))

            for gather in gathers:
                gather.start()

            for gather in gathers:
                gather.join()

            print(results)
            for num, date in enumerate(dates):
                csv_write.writerow({'date': date[0].format('YYYY/MM/DD'),
                                    'hour': date[0].format('HH'),
                                    'statistics': json.dumps(results[num]),
                                    'loc': loc,
                                    })
                result_total['counts'].update(results[num]['counts'])
                result_total['network_type'].update(
                    results[num]['network_type'])

    pprint(dict(result_total))


@cli.command('sheetrow', short_help='Convert raw data to rows format')
@click.option('--path', 'input_path', help='path of raw data, CSV format')
def sheetrow(input_path):
    ''' Convert raw data to rows format '''
    with open(input_path, 'r+', encoding='UTF8') as csv_files:
        csv_reader = csv.DictReader(csv_files)
        with open(f'./rows_{path.basename(input_path)}', 'w+', encoding='UTF8') as csv_save_files:
            csv_writer = csv.DictWriter(csv_save_files, fieldnames=(
                'loc', 'date', 'hour', 'asn', 'count'))
            csv_writer.writeheader()
            for raw in csv_reader:
                rows = []
                asns = json.loads(raw['statistics'])['counts']
                for asn, count in asns.items():
                    rows.append({'loc': raw['loc'], 'date': raw['date'], 'hour': raw['hour'],
                                'asn': asn, 'count': count, })
                csv_writer.writerows(rows)


if __name__ == '__main__':
    cli()
