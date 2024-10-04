from datetime import datetime
from decimal import Decimal
from shared_package.domain.funds.entities import Subscription, Fund
from shared_package.domain.funds.repositories import FundRepository


class FundLogic:
    def __init__(self):
        self.repository = FundRepository()

    async def subscribe_to_fund(self, user_id: str, fund_id: int, amount: float) -> str:
        user = self.repository.get_user_by_id()
        if not user:
            return "Usuario no encontrado."

        if user["balance"] < amount:
            return f"No tiene saldo suficiente para vincularse al fondo. Su balance actual es {user['balance']}."

        fund_data = self.repository.get_fund_by_id(fund_id)
        if not fund_data:
            return "Fondo no encontrado."

        # Instance
        fund = Fund(
            id=fund_data["uuid"],
            name=fund_data["name"],
            category=fund_data["category"],
            min_investment=fund_data["min_amount"],
        )

        if amount < fund.min_investment:
            return f"El monto mínimo de inversión para el fondo {fund.name} es {fund.min_investment}."

        existing_subscription = self.repository.get_user_subscription(user_id, fund_id)
        if existing_subscription:
            return f"Ya está suscrito al fondo {fund.name}."

        new_balance = user["balance"] - Decimal(str(amount))
        self.repository.update_user_balance(user_id, new_balance)

        # Create entity suscription
        subscription = Subscription(
            user_id=user_id, fund=fund, amount=amount, subscribed_at=datetime.now()
        )
        self.repository.transaction(subscription, transaction_type="suscribe")

        return f"Suscripción exitosa al fondo {fund.name}."

    async def cancel_subscription(self, user_id: int, fund_id: int) -> str:
        subscriptions = self.repository.get_user_subscription(user_id, fund_id)
        if not subscriptions:
            return "No se encontró ninguna suscripción activa a este fondo."
        subscription = subscriptions[0]
        amount = subscription["amount"]
        user = self.repository.get_user_by_id()
        new_balance = user["balance"] + Decimal(str(amount))
        self.repository.update_user_balance(user_id, new_balance)

        fund_data = self.repository.get_fund_by_id(fund_id)
        if not fund_data:
            return "Fondo no encontrado."

        fund = Fund(
            id=fund_data["uuid"],
            name=fund_data["name"],
            category=fund_data["category"],
            min_investment=fund_data["min_amount"],
        )

        subscription = Subscription(
            user_id=user_id, fund=fund, amount=amount, subscribed_at=datetime.now()
        )
        self.repository.transaction(subscription, transaction_type="cancel")
        return f"Suscripción {fund_id} cancelada exitosamente y el monto de {amount} ha sido retornado al balance del usuario."

    async def get_user_subscriptions(self, user_id: int):
        return await self.repository.get_user_subscriptions(user_id)

    async def get_funds(self):
        return await self.repository.get_funds()
