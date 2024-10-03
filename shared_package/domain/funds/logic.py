from datetime import datetime
from .entities import Subscription
from .repositories import FundRepository


class FundLogic:
    def __init__(self):
        self.repository = FundRepository()

    def subscribe_to_fund(self, user_id: int, fund_id: int, amount: float) -> str:
        fund = next((f for f in self.repository.funds if f.id == fund_id), None)

        if fund is None:
            return "Fondo no encontrado."

        if amount < fund.min_investment:
            return f"No tiene saldo disponible para vincularse al fondo {fund.name}."

        subscription = Subscription(
            user_id=user_id, fund=fund, amount=amount, subscribed_at=datetime.now()
        )
        self.repository.subscribe(subscription)
        return f"Suscripción exitosa al fondo {fund.name}."

    def cancel_subscription(self, user_id: int, fund_id: int) -> str:
        self.repository.cancel_subscription(user_id, fund_id)
        return "Suscripción cancelada exitosamente."

    def get_user_subscriptions(self, user_id: int):
        return self.repository.get_user_subscriptions(user_id)

    def get_funds(self):
        return self.repository.get_funds()
