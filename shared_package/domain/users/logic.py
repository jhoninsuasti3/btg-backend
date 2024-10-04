from shared_package.domain.users.repositories import UserRepository
from .entities import User

class UserLogic:
    def __init__(self):
        self.repository = UserRepository()

    async def create_user(self, email: str, balance: float) -> str:

        user = User(
            email=email,
            balance=balance,
        )

        await self.repository.create_user(user)
        return f"Usuario {email} creado con éxito."
