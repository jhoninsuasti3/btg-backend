from fastapi import APIRouter, FastAPI
import os
from .services import TransactionService
from .schemas import TransactionHistoryResponse
from mangum import Mangum

app = FastAPI(
    debug=os.getenv("DEBUG", False),
    title="Transactions Service",
)

router = APIRouter()

service = TransactionService()


@router.get("/history/{user_id}", response_model=TransactionHistoryResponse)
async def get_transaction_history(user_id: int):
    return await service.get_transaction_history(user_id)
