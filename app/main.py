from fastapi import FastAPI, Depends

from app.config import Settings, get_setting

app = FastAPI()
# uvicorn app.main:app --reload


@app.get("/ping")
async def pong(settings: Settings = Depends(get_setting)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }


@app.get("/")
def root():
    return {"message": "Hello"}