from fastapi import APIRouter, FastAPI
import os

from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    debug=os.getenv("DEBUG", False),
    title="Auth Service",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/auth")


@router.get("")
async def api_get_auth():
    return {"message": "Result api get"}


@router.get("/request_test")
async def api_get_auth():
    return {"message": "Result api get request_test"}


# @router.post("/cancel")
# async def cancel_subscription(request: CancelSubscriptionRequest):
#     result = await service.cancel_subscription(request)
#     return {"message": result}


# @router.get("/funds")
# async def get_funds():
#     funds = await service.get_funds()
#     return {"funds": funds}
app.include_router(router)
handler = Mangum(app)
