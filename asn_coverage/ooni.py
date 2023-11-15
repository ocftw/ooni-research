''' OONI '''
import gzip
import io
import json
from pprint import pprint

import boto3
from boto3.s3.transfer import TransferConfig
from botocore import UNSIGNED
from botocore.config import Config

client_config = Config(
    region_name='eu-central-1',
    user_agent='OCF.tw OONI-Research github.com/ocftw/ooni-research',
    signature_version=UNSIGNED,
    connect_timeout=120,
    read_timeout=120,
)
s3client = boto3.client('s3', config=client_config)
result = s3client.list_objects_v2(
    Bucket='ooni-data-eu-fra',
    Prefix='raw/20231110/09/TW/webconnectivity/',
    Delimiter='/',
)

pprint(result)

for file_info in result['Contents']:
    if not file_info['Key'].endswith('jsonl.gz'):
        continue

    print(file_info['Key'])
    with io.BytesIO() as file_obj:
        s3client.download_fileobj(Key=file_info['Key'],
                                  Bucket='ooni-data-eu-fra',
                                  Fileobj=file_obj,
                                  Config=TransferConfig())

        with gzip.GzipFile(fileobj=io.BytesIO(file_obj.getvalue())) as raw_data:
            for raw in raw_data:
                json_data = json.loads(raw)
                print(f"""[{json_data['probe_asn']} - {
                    json_data['probe_cc']}] {json_data['resolver_asn']} {
                    json_data['resolver_ip']} {json_data['resolver_network_name']}""")
