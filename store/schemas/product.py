from decimal import Decimal
from typing import Annotated, Optional
from bson import Decimal128
from pydantic import AfterValidator, Field
from store.schemas.base import BaseSchemasMixin, OutSchema


class ProductBase(BaseSchemasMixin):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: Decimal = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductInn(ProductBase, BaseSchemasMixin): ...


class ProductOut(ProductIn, OutSchema): ...
