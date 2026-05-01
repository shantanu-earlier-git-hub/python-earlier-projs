from pydantic import BaseModel, ConfigDict, Field


class CreateProductModel(BaseModel):
    product_name: str = Field(..., description="Product name")
    price: float = Field(..., gt=0, description="Product price")
    isavailable: bool = Field(..., description="Product availability")


class ProductModel(BaseModel):
    id: int = Field(..., gt=0, description="Product ID")
    product_name: str = Field(..., description="Product name")
    price: float = Field(..., gt=0, description="Product price")
    isavailable: bool = Field(..., description="Product availability")

    model_config = ConfigDict(from_attributes=True)
