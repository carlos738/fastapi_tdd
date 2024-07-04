from datetime import datetime
# from decimal import Decimal
# from bson import Decimal128
from pydantic import Field, UUID4, BaseModel


class BaseSchemaMixin(BaseModel):
    class Config:
        from_attributes = True


class OutSchema(BaseModel):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
