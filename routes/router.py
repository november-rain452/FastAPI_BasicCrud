from fastapi import APIRouter
from routes import user_routes,product_routes,orders_routes

api_router = APIRouter()

api_router.include_router(user_routes.router)
api_router.include_router(product_routes.router)
api_router.include_router(orders_routes.router)