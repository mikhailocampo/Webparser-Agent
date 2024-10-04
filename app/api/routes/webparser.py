from fastapi import APIRouter, Depends
from app.dependencies import verify_api_key

router = APIRouter(dependencies=[Depends(verify_api_key)])


@router.post("/")
async def handle_webparser_request():
    return {"message": "Hello World"}
