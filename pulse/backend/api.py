''' API '''
from fastapi import FastAPI
from routers import vega

TAG_META = [
    {'name': 'vega', 'description': 'For Vega-Lite output graphics.'}
]

app = FastAPI(
    title="OCF OONI-Research API",
    description="Store daily observational datas.",
    version="2025.03.31",
    root_path="/api",
    openapi_tags=TAG_META,
    contact={
        'name': 'OCF OONI-Research Team',
        'url': 'https://ooni-research.ocf.tw/',
        'email': 'ooni-research@ocf.tw',
    },
    license_info={
        'name': 'GPL-3.0',
        'url': 'https://github.com/ocftw/ooni-research/blob/main/asn_coverage/LICENSE',
    }
)
app.include_router(vega.router)

@app.get('/')
async def main():
    ''' main page '''
    return {'Hello': "world"}
