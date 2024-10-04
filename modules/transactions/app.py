from fastapi import APIRouter, FastAPI
import os
from .services import TransactionService
from .schemas import TransactionHistoryResponse
from mangum import Mangum
from starlette.requests import Request

app = FastAPI(
    debug=os.getenv("DEBUG", False),
    title="Transactions Service",
)

router = APIRouter(prefix="/transactions")

service = TransactionService()


@router.get("")
async def get_transaction_history(request : Request):
    return await service.get_transactions()


app.include_router(router)
handler = Mangum(app)