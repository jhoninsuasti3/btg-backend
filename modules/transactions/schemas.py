from pydantic import BaseModel
from typing import List


class TransactionResponse(BaseModel):
    id: str
    user_id: int
    fund_name: str
    amount: float
    transaction_type: str
    timestamp: str


class TransactionHistoryResponse(BaseModel):
    transactions: List[TransactionResponse]
