from fastapi import APIRouter, Depends
from src.services.products import product_marketplace_services
from fastapi.security.api_key import APIKey
from src.auth.api_auth import get_api_key
from src.schemas.product_schema.product_schema import ProductReviewData

from src.log_conf import Logger
logger = Logger.get_logger(__name__)

router = APIRouter()


@router.post('/get_product_reviews')
async def get_product_reviews(request_payload: ProductReviewData, api_key: APIKey = Depends(get_api_key)):
    """This is a controller function for getting product reviews"""
    logger.info("#src #api #endpoints #products #products.py get_product_data starts..")
    response = product_marketplace_services.get_product_reviews(request_payload)
    return response
