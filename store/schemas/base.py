# from datetime import datetime
# from decimal import Decimal
# from bson import Decimal128
# from pydantic import UUID4, BaseModel, Field, model_validator


class BaseSchemaMixin(BaseModel):
    class Config:
        from_attributes = True
