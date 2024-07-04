# from datetime import datetime
# from decimal import Decimal
# from bson import Decimal128
from pydantic import BaseModel


class BaseSchemaMixin(BaseModel):
    class Config:
        from_attributes = True
