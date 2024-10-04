from fastapi import Header, HTTPException, Depends
from app.core.config import get_app_settings
from app.core.settings.app import AppSettings


async def verify_api_key(
    authorization: str = Header(...), settings: AppSettings = Depends(get_app_settings)
) -> None:
    if not settings.validate_authorization(authorization):
        raise HTTPException(status_code=403, detail="Invalid API Key")
