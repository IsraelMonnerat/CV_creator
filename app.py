import logging
from fastapi import FastAPI
from routers import cv_creator


def add_routes(app: FastAPI) -> None:
    prefix = "/cv-creator/api"
    app.include_router(cv_creator.router, prefix=prefix)


def create_app() -> FastAPI:
    app = FastAPI(
        title="CV Creator",
        version="1.1.0",
        description="Create your CV with ease",
        docs_url="/docs",
    )
    logging.info("Adding routes")
    add_routes(app)
    return app
