from shared_package.domain.funds.entities import Subscription, Fund
from shared_package.constants import client_dynamo, EnvironmentVariables
from boto3.dynamodb.conditions import Key, Attr
from decimal import Decimal


class FundRepository:
    def __init__(self):
        self.subscriptions = []
        self.table_fund = client_dynamo.Table(EnvironmentVariables.FOUNDS_TABLE_NAME)
        self.subscriptions_table = client_dynamo.Table(EnvironmentVariables.TRANSACTIONS_TABLE_NAME)
        self.table_user = client_dynamo.Table(EnvironmentVariables.USERS_TABLE_NAME)

    def save_subscription(self, subscription: Subscription):
        self.subscriptions_table.put_item(Item={
            'uuid': subscription.id,
            'user_id': str(subscription.user_id),
            'fund_id': subscription.fund.id,
            'fund_name': subscription.fund.name,
            'amount': Decimal(str(subscription.amount)),
            'subscribed_at': subscription.subscribed_at.isoformat()
        })

    def cancel_subscription(self,  user_id: str, fund_id: str):
        response = self.subscriptions_table.query(
            IndexName='User-index',
            KeyConditionExpression=Key('user_id').eq(str(user_id)),
            FilterExpression=Attr('fund_id').eq(str(fund_id)) # Filter by fund_id
        )

        items = response.get('Items', [])

        if items:
            item = items[0]
            self.subscriptions_table.delete_item(Key={'uuid': item['uuid']})
            return "Cancelled done"
        else:
            return "Subscription not found"

    def get_user_subscription(self, user_id: str, fund_id: str):
        response = self.subscriptions_table.query(
            IndexName='User-index',
            KeyConditionExpression=Key('user_id').eq(str(user_id)),
            FilterExpression=Attr('fund_id').eq(str(fund_id)) # Filter by fund_id
        )
        items = response.get('Items', [])

        return items



    async def get_funds(self):
        response = self.table_fund.scan()
        return response.get('Items', [])

    def get_fund_by_id(self, uuid: str):
        response = self.table_fund.get_item(Key={'uuid': uuid})
        return response.get('Item')

    def get_user_by_id(self):
        response =  self.table_user.scan(Limit=1)  # Limitamos a 1 para obtener solo el primer usuario
        users = response.get('Items', [])

        if not users:
            raise ValueError("No se encontró ningún usuario en la tabla.")

        return users[0]

    def update_user_balance(self, user_id: str, new_balance: float):
        self.table_user.update_item(
            Key={'uuid': user_id},
            UpdateExpression="SET balance = :balance",
            ExpressionAttributeValues={':balance': Decimal(str(new_balance))}
        )
