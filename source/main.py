from fastapi import FastAPI
from routes import base,data
from dotenv import load_dotenv

load_dotenv()

app=FastAPI()

app.include_router(base.base_router)
app.include_router(data.base_router)