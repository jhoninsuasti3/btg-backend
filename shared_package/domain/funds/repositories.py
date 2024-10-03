from typing import List
from .entities import Subscription, Fund


class FundRepository:
    def __init__(self):
        self.subscriptions = []
        self.funds = [
            Fund(
                id=1,
                name="FPV_BTG_PACTUAL_RECAUDADORA",
                category="FPV",
                min_investment=75000,
            ),
            Fund(
                id=2,
                name="FPV_BTG_PACTUAL_ECOPETROL",
                category="FPV",
                min_investment=125000,
            ),
            Fund(id=3, name="DEUDAPRIVADA", category="FPV", min_investment=50000),
            Fund(id=4, name="FDO-ACCIONES", category="FIC", min_investment=250000),
            Fund(
                id=5,
                name="FPV_BTG_PACTUAL_DINAMICA",
                category="FIC",
                min_investment=100000,
            ),
        ]

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
        return self.funds
