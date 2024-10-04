from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


async def http422_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    errors = exc.errors() if callable(exc.errors) else exc.errors
    return JSONResponse({"errors": errors}, status_code=422)
