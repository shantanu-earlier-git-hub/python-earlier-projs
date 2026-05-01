from typing import TypedDict


class ProductType(TypedDict):
    price: float
    prodId: int
    quantity: int
    item: str
    type: str
