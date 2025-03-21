""" Route Vega-Lite """
from fastapi import APIRouter, status
from pgdb import PGConn
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

router = APIRouter(
    prefix='/vega',
    tags=['vega', ],
    responses={status.HTTP_404_NOT_FOUND: {'description': 'Not found'}},
)

class Country(Enum):
    tw = 'tw'

class RelaysRunning(BaseModel):
    created_at: datetime
    count: int
    running: bool = Field(default=False)
    observed_bandwidth: float = Field(default=0)

class RelaysVersion(BaseModel):
    created_at: datetime
    count: int
    version: str = Field(default="")

class RelaysASN(BaseModel):
    created_at: datetime
    count: int
    asn: str


@router.get('/tor/relays/running')
async def tor_relays_running(country: Country) -> list[RelaysRunning]:
    ''' Get Tor Relays Running by country'''
    datas = []
    with PGConn() as pg_conn:
        for row in pg_conn.cur.execute('''select date(created_at) as dt,
                                                 count(DISTINCT fingerprint),
                                                 running,
                                                 round(sum(observed_bandwidth)/count(date(created_at))*count(DISTINCT fingerprint), 4)
                                       from relay_details
                                       where country=%s
                                       group by dt, running
                                       order by dt, running
                                      ;''', (country, )):
            datas.append(RelaysRunning(created_at=row[0], count=row[1], running=row[2], observed_bandwidth=row[3]))

    return datas

@router.get('/tor/relays/version')
async def tor_relays_version(country: Country) -> list[RelaysVersion]:
    '''Get Tor Relays Version by country'''
    datas = []
    with PGConn() as pg_conn:
        for row in pg_conn.cur.execute('''
                                       select date(created_at) as dt,
                                              count(DISTINCT fingerprint),
                                              version
                                       from relay_details
                                       where country=%s
                                       group by dt, version
                                       order by dt, version desc;
                                      ;''', (country, )):
            datas.append(RelaysVersion(created_at=row[0], count=row[1], version=row[2]))

    return datas

@router.get('/tor/relays/asn')
async def tor_relays_asn(country: Country) -> list[RelaysASN]:
    '''Get Tor Relays Version by country'''
    datas = []
    with PGConn() as pg_conn:
        for row in pg_conn.cur.execute('''
                                       select date(created_at) as dt,
                                              count(DISTINCT fingerprint),
                                              asn
                                       from relay_details
                                       where country=%s
                                       group by dt, asn
                                       order by dt, asn;
                                      ;''', (country, )):
            datas.append(RelaysASN(created_at=row[0], count=row[1], asn=row[2]))

    return datas