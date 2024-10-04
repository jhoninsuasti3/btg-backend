from fastapi import APIRouter, FastAPI
import os
from services import TransactionService
from schemas import TransactionHistoryResponse
from mangum import Mangum
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    debug=os.getenv("DEBUG", False),
    title="Transactions Service",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
router = APIRouter(prefix="/transactions")

service = TransactionService()


@router.get("")
async def get_transaction_history(request: Request):
    return await service.get_transactions()


app.include_router(router)
handler = Mangum(app)
