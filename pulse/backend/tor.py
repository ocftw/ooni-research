""" Fetch tor metrics

    https://metrics.torproject.org/onionoo.html

"""
from datetime import datetime
from pprint import pprint

import click
from pydantic import BaseModel, Field
from requests.sessions import Session


class TorMetrics(Session):
    ''' Fetch Tor Metrics '''

    def get_relays(self, country='tw'):
        ''' Get Relays '''
        return self.get('https://onionoo.torproject.org/details',
                        params={'country': country}).json()


class Relay(BaseModel):
    ''' Relay Structs '''
    nickname: str
    fingerprint: str
    running: bool
    measured: bool
    asn: str = Field(alias='as')
    as_name: str
    consensus_weight: int
    platform: str
    version: str
    contact: str = ""
    flags: list[str]
    first_seen: datetime
    last_seen: datetime
    last_changed: datetime = Field(alias='last_changed_address_or_port')
    bandwidth_rate: int
    bandwidth_burst: int
    observed_bandwidth: int
    advertised_bandwidth: int
    guard_probability: float = 0
    middle_probability: float = 0
    exit_probability: float = 0


@click.group()
def cli():
    ''' cli for groups '''


@cli.command('details', short_help='Get tor nodes details')
@click.option('--country', default='tw', help='country code')
def details(country='tw'):
    ''' Get details '''
    resp_relays = TorMetrics().get_relays(country=country)
    relays = []

    for relay in resp_relays['relays']:
        relays.append(Relay.model_validate(relay))

    bandwidth = 0
    for relay in relays:
        bandwidth += relay.observed_bandwidth
        pprint(relay)

    print(
        f'bandwidth: {bandwidth/1000/1000:.4f} MB/s ({bandwidth/1000/1000*8:.4f} Mb/s)')


if __name__ == '__main__':
    cli()
