from shared_package.constants import client_dynamo, EnvironmentVariables
from shared_package.domain.users.entities import User
from decimal import Decimal


class UserRepository:
    def __init__(self):
        self.users_table = client_dynamo.Table(EnvironmentVariables.USERS_TABLE_NAME)

    async def create_user(self, user: User):
        self.users_table.put_item(
            Item={
                "uuid": user.id,
                "email": user.email,
                "balance": Decimal(str(user.balance)),
            }
        )
