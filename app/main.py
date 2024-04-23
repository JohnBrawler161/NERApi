import uvicorn
from fastapi import FastAPI

from app.settings import settings
from app.ner_router import router


def include_router(app: FastAPI):
    app.include_router(router)


def create_app() -> FastAPI:
    app = FastAPI()
    include_router(app)

    return app


if __name__ == '__main__':
    uvicorn.run("app.main:create_app", host=settings.host, port=settings.port, reload=settings.reload)
