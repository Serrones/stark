  
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from dynaconf import settings

world = settings.get('WORLD')


app = FastAPI(
    title="Welcome to Stark CMS", openapi_url=f"/stark/openapi.json"
)

@app.get('/')
def read_root():
    return {"Hello": world}

@app.get('/test/')
def read_root():
    return {"Hello": world}