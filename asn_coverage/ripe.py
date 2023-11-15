""" Main """
import re

from requests import Response, Session


class RIPEData(Session):
    ''' Fetch RIPE Data '''

    def __init__(self) -> None:
        super().__init__()
        self.url = 'https://ftp.ripe.net'

    def fetch_asn(self) -> Response:
        ''' Fetch ASN name '''
        return super().get(self.url+'/ripe/asnames/asn.txt')

    def get_asn_name(self):
        ''' Get and Process ASN Data '''
        asn_data = self.fetch_asn()
        pattens = (
            re.compile(
                r"(?P<no>\d+) (?P<r>-Reserved AS-), (?P<location>[A-Z]{2})"),
            re.compile(
                r"(?P<no>\d+) (?P<org_id>[\w\-]+)? ?(?P<registrar>[\w\ \-\.\&\,\(\)\"/@:?#*'`!+\]\[]+)?, (?P<location>[A-Z]{2})"),
            re.compile(r"(?P<no>23456) (?P<name>.+)"),
        )

        result = []
        for raw in asn_data.text.split('\n'):
            if not raw:
                continue

            for splitor in pattens:
                matched = splitor.match(raw)
                if matched:
                    result.append(matched.groupdict())
                    break
            else:
                raise NotImplementedError(f'`{raw}`')
        return result


if __name__ == '__main__':
    for asn in RIPEData().get_asn_name():
        if 'location' in asn and asn['location'] == 'TW':
            print(asn)
