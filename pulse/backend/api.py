''' API '''
from fastapi import FastAPI
from routers import vega

app = FastAPI()
app.include_router(vega.router)

@app.get('/')
async def main():
    ''' main page '''
    return {'Hello': "world"}
