from fastapi import APIRouter, FastAPI
import os
from services import FundService
from schemas import SubscribeRequest, CancelSubscriptionRequest
from mangum import Mangum
from starlette.requests import Request

app = FastAPI(
    debug=os.getenv("DEBUG", False),
    title="Funds Service",
)


router = APIRouter(prefix="/founds")

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


@router.get("/funds")
async def api_get_funds():
    funds = await service.get_funds()
    return {"funds": funds}


app.include_router(router)
handler = Mangum(app)
