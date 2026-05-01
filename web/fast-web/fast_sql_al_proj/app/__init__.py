from app.dependencies import app
from app.routes.productroute import product_router

app.include_router(product_router)
