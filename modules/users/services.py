from shared_package.domain.users.logic import UserLogic
from schemas import UserCreate

class UserService:
    def __init__(self):
        self.logic = UserLogic()

    async def create_user(self, request: UserCreate) -> str:
        return await self.logic.create_user(
            email=request.email,
            balance=request.balance
        )
