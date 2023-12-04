''' OONI '''
import gzip
import io
import json
from pprint import pprint

import boto3
import click
from arrow import Arrow
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


@click.command()
@click.option('--units', default=36, help='lookback by hours')
@click.option('--loc', default='TW', help='location')
def lookback(units=36, loc='TW'):
    ''' lookback the datas '''
    oonis3 = OONIS3()
    counts = {}
    network_type = {}
    for date in Arrow.span_range('hour',
                                 Arrow.utcnow().shift(hours=units*-1).datetime,
                                 Arrow.utcnow().datetime):
        result = count_asn(date=date[0], loc=loc, oonis3=oonis3)

        for asn, value in result['counts'].items():
            if asn not in counts:
                counts[asn] = 0
            counts[asn] += value

        for nw_type, value in result['network_type'].items():
            if nw_type not in network_type:
                network_type[nw_type] = 0
            network_type[nw_type] += value

    pprint(counts)
    pprint(network_type)


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


def span_date():
    ''' Span date '''
    for date in Arrow.span_range('hour',
                                 Arrow.utcnow().shift(hours=-10).datetime,
                                 Arrow.utcnow().datetime):
        print(date)
        print(date[0].format('YYYYMMDD'))
        print(date[0].format('HH'))


if __name__ == '__main__':
    lookback()
    # span_date()
