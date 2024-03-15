from datetime import datetime

from src.routes import student
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.exception import UnicornException

app = FastAPI()

app.include_router(student.router)


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"msg": exc.name, "time": "2122"},
    )
