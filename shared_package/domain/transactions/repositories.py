from boto3.dynamodb.conditions import Key
from shared_package.constants import client_dynamo, EnvironmentVariables


class TransactionRepository:
    def __init__(self):
        self.subscriptions_table = client_dynamo.Table(
            EnvironmentVariables.TRANSACTIONS_TABLE_NAME
        )

    async def get_user_transactions(self):
        response = self.subscriptions_table.scan()
        return response.get("Items", [])
