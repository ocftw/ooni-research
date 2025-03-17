""" Fetch tor metrics

    https://metrics.torproject.org/onionoo.html

"""
import logging
import sys
from pprint import pprint
from sqlite3 import SQLITE_DBCONFIG_LEGACY_FILE_FORMAT
from structs import Relay
from tor_onionoo import TorOnionoo

import click


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(stream=sys.stdout), ],
)

logger = logging.getLogger('tor-details')

@click.group()
def cli():
    ''' cli for groups '''


@cli.command('details', short_help='Get tor nodes details')
@click.option('--country', default='tw', help='country code')
def details(country='tw'):
    ''' Get details '''
    resp_details = TorOnionoo().get_details(country=country)

    bandwidth = 0
    for relay in resp_details.relays:
        bandwidth += relay.observed_bandwidth
        logger.info(relay)

    logger.info(
        f'bandwidth: {bandwidth/1000/1000:.4f} MB/s ({bandwidth/1000/1000*8:.4f} Mb/s)')
    logger.info(f'relays: {len(resp_details.relays)}')


if __name__ == '__main__':
    cli()
