from fastapi import APIRouter, FastAPI
import os
from .services import UserService
from mangum import Mangum
from starlette.requests import Request
from .schemas import UserCreate

app = FastAPI(
    debug=os.getenv("DEBUG", False),
    title="Funds Service",
)


router = APIRouter(prefix="/users")

service = UserService()


@router.post("")
async def create_user(request: Request, suscribe_body: UserCreate):
    result = await service.create_user(suscribe_body)
    return {"message": result}


app.include_router(router)
handler = Mangum(app)
