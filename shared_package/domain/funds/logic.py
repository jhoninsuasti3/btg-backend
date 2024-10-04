from datetime import datetime
from .entities import Subscription, Fund
from .repositories import FundRepository

class FundLogic:
    def __init__(self):
        self.repository = FundRepository()

    async def subscribe_to_fund(self, user_id: int, fund_id: int, amount: float) -> str:
        if amount < 500000:
            return "El monto mínimo para abrir una suscripción es de COP $500,000."

        fund_data =  self.repository.get_fund_by_id(fund_id)
        if not fund_data:
            return "Fondo no encontrado."

        # Instance
        fund = Fund(
            id=fund_data['uuid'],
            name=fund_data['name'],
            category=fund_data['category'],
            min_investment=fund_data['min_amount']
        )
        if amount < fund.min_investment:
            return f"No tiene saldo disponible para vincularse al fondo {fund.name}. El monto mínimo es {fund.min_investment}."

        existing_subscription =  self.repository.get_user_subscription(user_id, fund_id)
        if existing_subscription:
            return f"Ya está suscrito al fondo {fund.name}."
        # Create entity suscription
        subscription = Subscription(
            user_id=user_id,
            fund=fund,
            amount=amount,
            subscribed_at=datetime.now()
        )
        self.repository.save_subscription(subscription)

        return f"Suscripción exitosa al fondo {fund.name}."


    async def cancel_subscription(self, user_id: int, fund_id: int) -> str:
        return self.repository.cancel_subscription(user_id, fund_id)

    async def get_user_subscriptions(self, user_id: int):
        return await self.repository.get_user_subscriptions(user_id)

    async def get_funds(self):
        return await self.repository.get_funds()
