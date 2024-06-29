from fastapi import APIRouter
from store.controllers.product import routers as product

api_router = APIRouter()
api_router.include_router(product, prefix="/products")
