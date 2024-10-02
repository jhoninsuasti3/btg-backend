from pydantic import BaseModel
from typing import List

class SubscribeRequest(BaseModel):
    user_id: int
    fund_id: int
    amount: float

class CancelSubscriptionRequest(BaseModel):
    user_id: int
    fund_id: int

class FundResponse(BaseModel):
    id: int
    name: str
    min_investment: float
    category: str
