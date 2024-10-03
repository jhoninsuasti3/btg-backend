from typing import List
from shared_package.domain.funds.entities import Subscription, Fund
from shared_package.constants import client_dynamo, EnvironmentVariables


class FundRepository:
    def __init__(self):
        self.subscriptions = []
        self.table_fund = client_dynamo.Table(EnvironmentVariables.FOUNDS_TABLE_NAME)

    def subscribe(self, subscription: Subscription):
        self.subscriptions.append(subscription)

    def cancel_subscription(self, user_id: int, fund_id: int):
        self.subscriptions = [
            sub
            for sub in self.subscriptions
            if not (sub.user_id == user_id and sub.fund.id == fund_id)
        ]

    def get_user_subscriptions(self, user_id: int) -> List[Subscription]:
        return [sub for sub in self.subscriptions if sub.user_id == user_id]

    def get_funds(self):
        response = self.table_fund.scan()
        return response["Items"]
