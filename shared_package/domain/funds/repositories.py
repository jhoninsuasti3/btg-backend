from shared_package.domain.funds.entities import Subscription, Fund
from shared_package.constants import client_dynamo, EnvironmentVariables
from boto3.dynamodb.conditions import Key
from decimal import Decimal


class FundRepository:
    def __init__(self):
        self.subscriptions = []
        self.table_fund = client_dynamo.Table(EnvironmentVariables.FOUNDS_TABLE_NAME)
        self.subscriptions_table = client_dynamo.Table(EnvironmentVariables.TRANSACTIONS_TABLE_NAME)

    def save_subscription(self, subscription: Subscription):
        self.subscriptions_table.put_item(Item={
            'uuid': subscription.id,
            'user_id': str(subscription.user_id),
            'fund_id': subscription.fund.id,
            'fund_name': subscription.fund.name,
            'amount': Decimal(str(subscription.amount)),
            'subscribed_at': subscription.subscribed_at.isoformat()
        })

    def cancel_subscription(self, uuid: str, user_id: str):
        print("-*/*-/"*10)
        print(uuid)
        print(user_id)
        response = self.subscriptions_table.get_item(Key={'uuid': uuid})
        print(response)
        item = response.get('Item')
        print(item)
        if item and item.get('user_id') == str(user_id):
            self.subscriptions_table.delete_item(Key={'uuid': uuid})
            return "Cancelled done"
        else:
            return "Subs not found"

    def get_user_subscription(self, user_id: str, fund_id: str):
        user_id = str(user_id)
        fund_id = str(fund_id)
        # usar 'user_id' en la KeyConditionExpression si es la clave de partición
        response = self.subscriptions_table.query(
            IndexName='User-index',
            KeyConditionExpression=Key('user_id').eq(user_id)
        )

        items = response.get('Items', [])

        return [item for item in items if item.get('fund_id') == fund_id]



    async def get_funds(self):
        response = self.table_fund.scan()
        return response.get('Items', [])

    def get_fund_by_id(self, uuid: str):
        response = self.table_fund.get_item(Key={'uuid': uuid})
        return response.get('Item')

