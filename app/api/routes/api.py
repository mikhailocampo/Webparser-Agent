from fastapi import APIRouter
from app.api.routes import webparser

router = APIRouter(
    prefix="/api/v1",
)

router.include_router(webparser.router, prefix="/webparser", tags=["webparser"])
