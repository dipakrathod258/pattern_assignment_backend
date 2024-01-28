from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.server import create_app
from src.api.api import api_router

import logging
import uvicorn


# Creating FastAPI App here
app: FastAPI = create_app()
app.include_router(api_router, prefix='/api/v1')

origins = ["http://localhost:3000", '*',]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def run_server() -> None:
    """This function is for running the FastAPI app using Uvicorn package"""
    logging.info("Pattern server is running...")
    uvicorn.run(
        app,
        host='127.0.0.1',
        port=8000,
        log_level='debug',
    )
