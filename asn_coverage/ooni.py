''' OONI '''
import gzip
import io
import json
from pprint import pprint

import boto3
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


def lookback(units=36):
    ''' lookback the datas '''
    oonis3 = OONIS3()
    counts = {}
    for date in Arrow.span_range('hour',
                                 Arrow.utcnow().shift(hours=units*-1).datetime,
                                 Arrow.utcnow().datetime):
        result = oonis3.list_webconnectivity(
            date=date[0].format('YYYYMMDD'),
            hour=date[0].format('HH'),
        )

        pprint(result)

        if 'Contents' not in result:
            continue

        for file_info in result['Contents']:
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
                        if json_data['probe_asn'] not in counts:
                            counts[json_data['probe_asn']] = 0

                        counts[json_data['probe_asn']] += 1

                        # print(f"""[{json_data['probe_asn']} - {
                        #    json_data['probe_cc']}] {json_data['resolver_asn']} {
                        #    json_data['resolver_ip']} {json_data['resolver_network_name']}""")

        pprint(counts)

    pprint(counts)


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
