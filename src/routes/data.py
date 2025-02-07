from fastapi import FastAPI,APIRouter,Depends
from helpers.config import get_settings,Settings

base_router = APIRouter(
     prefix="/api/v1",
    tags=["api_v1"],
)
