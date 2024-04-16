from pydantic import BaseModel, Field
from datetime import datetime

class PromotionBase(BaseModel):
    name: str = Field(..., description="The name of the promotion")
    description: str = Field(..., description="The description of the promotion")
    end_date: datetime = Field(..., description="The end date of the promotion")

class PromotionCreate(PromotionBase):
    pass

class PromotionRead(PromotionBase):
    id: int
    start_date: datetime = Field(..., description="The start date of the promotion")

    class Config:
        orm_mode = True
