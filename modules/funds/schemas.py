from pydantic import BaseModel
from typing import List


class SubscribeRequest(BaseModel):
    user_id: int
    fund_id: str
    amount: float


class CancelSubscriptionRequest(BaseModel):
    user_id: int
    fund_id: str


class FundResponse(BaseModel):
    id: int
    name: str
    min_investment: float
    category: str
