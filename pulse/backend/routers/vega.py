""" Route Vega-Lite """
from fastapi import APIRouter, status
from pgdb import PGConn
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

router = APIRouter(
    prefix='/vega',
    tags=['vega', ],
    responses={status.HTTP_404_NOT_FOUND: {'description': 'Not found'}},
)

class Country(Enum):
    tw = 'tw'

class Relays(BaseModel):
    created_at: datetime
    count: int
    running: bool
    observed_bandwidth: float

class ResponseRelays(BaseModel):
    country: Country
    result: list[Relays]


@router.get('/tor_relays')
async def tor_relays(country: Country) -> ResponseRelays:
    ''' Get Tor Relays by country'''
    datas = []
    with PGConn() as pg_conn:
        for row in pg_conn.cur.execute('''select date(created_at) as dt,
                                                 count(DISTINCT fingerprint),
                                                 running,
                                                 round(sum(observed_bandwidth)/count(date(created_at))*count(DISTINCT fingerprint), 4)
                                       from relay_details
                                       group by dt, running
                                       order by dt, running
                                      ;'''):
            datas.append(Relays(created_at=row[0], count=row[1], running=row[2], observed_bandwidth=row[3]))
    
    return ResponseRelays(country=country, result=datas)