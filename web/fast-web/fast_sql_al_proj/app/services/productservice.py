from typing import Union, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.entities.product import DbProduct
from app.models.productmodels import CreateProductModel, ProductModel


async def create_product(product: CreateProductModel, db_session: AsyncSession) -> ProductModel:
    new_product = DbProduct(**product.model_dump())
    db_session.add(new_product)
    await db_session.commit()
    await db_session.refresh(new_product)
    return ProductModel.model_validate(new_product)


async def update_product(product_id: int, product: ProductModel, db_session: AsyncSession) -> ProductModel:
    found_product = await find_product_by_id(product_id, db_session)

    for att, value in product.model_dump().items():
        setattr(found_product, att, value)

    print(found_product)
    db_session.add(found_product)
    await db_session.commit()
    await db_session.refresh(found_product)
    product = ProductModel.model_validate(found_product)
    print(f"product updated -> {product}")
    return product


async def delete_product(product_id: int, db_session: AsyncSession) -> str:
    found_product = await find_product_by_id(product_id, db_session)
    await db_session.delete(found_product)
    await db_session.commit()
    return f"deleted product ->  {product_id}"


async def find_product_by_id(product_id: int, db_session: AsyncSession) -> Union[DbProduct, None]:
    result = await db_session.execute(select(DbProduct).filter(DbProduct.id == product_id))
    return result.scalar_one_or_none()


async def find_all_products(db_session: AsyncSession) -> Union[list[ProductModel], None]:
    result = await db_session.execute(select(DbProduct).order_by(DbProduct.id.desc()))
    products = result.scalars().all()
    return [ProductModel.model_validate(product) for product in products]


async def create_many_products(products: list[CreateProductModel], db_session: AsyncSession) -> Union[
    list[ProductModel], None]:
    product_list = list([])

    db_products = [DbProduct(**product.model_dump()) for product in products]
    db_session.add_all(db_products)
    await db_session.commit()

    for db_product in db_products:
        await db_session.refresh(db_product)
        product_model = ProductModel.model_validate(db_product)
        product_list.append(product_model)

    return product_list
