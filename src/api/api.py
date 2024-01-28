from fastapi import APIRouter
from src.api.endpoints.products import product_controller

api_router = APIRouter()

api_router.include_router(product_controller.router, prefix="/products", tags=["Product APIs"])
