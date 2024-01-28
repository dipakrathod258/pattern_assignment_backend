from fastapi import FastAPI

import logging


def create_app() -> FastAPI:
    """This App create FastAPI app and sets the title and description on its Swagger UI"""
    try:
        logging.info("#src #core #server.py #create_app Initializing Pattern app")
        fast_app = FastAPI(
            title="Pattern Backend",
            description='It is a microservice that provides REST APIs & the source of data here is the Amazon '
                        'Rainforest APIs.'
        )
        return fast_app
    except Exception as error:
        logging.error(f"#src #core #server.py #create_app #ERROR = {str(error)}")
