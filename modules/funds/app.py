from fastapi import APIRouter, FastAPI
import os
from services import FundService
from schemas import SubscribeRequest, CancelSubscriptionRequest
from mangum import Mangum
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    debug=os.getenv("DEBUG", False),
    title="Funds Service",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
router = APIRouter(prefix="/funds")

service = FundService()


@router.post("/subscribe")
async def api_subscribe(request: Request, suscribe_body: SubscribeRequest):
    result = await service.subscribe(suscribe_body)
    return {"message": result}


@router.post("/cancel")
async def api_cancel_subscription(
    request: Request, cancel_suscription_body: CancelSubscriptionRequest
):
    result = await service.cancel_subscription(cancel_suscription_body)
    return {"message": result}


@router.get("")
async def api_get_funds():
    funds = await service.get_funds()
    return {"funds": funds}


app.include_router(router)
handler = Mangum(app)
