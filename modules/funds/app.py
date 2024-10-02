from fastapi import APIRouter, FastAPI
import os
from .services import FundService
from .schemas import SubscribeRequest, CancelSubscriptionRequest
from mangum import Mangum

app = FastAPI(
    debug=os.getenv("DEBUG", False),
    title="Funds Service",
)


router = APIRouter()

service = FundService()

@router.post("/subscribe")
async def subscribe(request: SubscribeRequest):
    result = await service.subscribe(request)
    return {"message": result}

@router.post("/cancel")
async def cancel_subscription(request: CancelSubscriptionRequest):
    result = await service.cancel_subscription(request)
    return {"message": result}

@router.get("/funds")
async def get_funds():
    funds = await service.get_funds()
    return {"funds": funds}

