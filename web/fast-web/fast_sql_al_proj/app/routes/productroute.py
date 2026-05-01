from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.models.productmodels import ProductModel, CreateProductModel
from app.services.productservice import find_all_products, create_product, create_many_products, delete_product, \
    update_product

product_router = APIRouter(prefix="/product", tags=["product"])


@product_router.post("/", response_model=ProductModel)
async def add_new_product(product: CreateProductModel, db_session: AsyncSession = Depends(get_db)):
    return await create_product(product, db_session)


@product_router.get("/all", response_model=list[ProductModel])
async def all_products(db_session: AsyncSession = Depends(get_db)):
    return await find_all_products(db_session)


@product_router.post("/add-many", response_model=list[ProductModel])
async def add_many_products(products: list[CreateProductModel], db_session: AsyncSession = Depends(get_db)):
    return await create_many_products(products, db_session)


@product_router.delete("/delete/{product_id}", response_model=list[ProductModel])
async def delete_one_product(product_id: int, db_session: AsyncSession = Depends(get_db)):
    return await delete_product(product_id, db_session)


@product_router.put("/update/{product_id}", response_model=list[ProductModel])
async def update_one_product(product_id: int, product: ProductModel, db_session: AsyncSession = Depends(get_db)):
    return await update_product(product_id, product, db_session)
