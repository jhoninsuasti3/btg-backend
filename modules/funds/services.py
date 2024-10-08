from shared_package.domain.funds.logic import FundLogic
from schemas import SubscribeRequest, CancelSubscriptionRequest, FundResponse
from typing import List


class FundService:
    def __init__(self):
        self.logic = FundLogic()

    async def subscribe(self, request: SubscribeRequest) -> str:
        return await self.logic.subscribe_to_fund(
            user_id=request.user_id, fund_id=request.fund_id, amount=request.amount
        )

    async def cancel_subscription(self, request: CancelSubscriptionRequest) -> str:
        return await self.logic.cancel_subscription(request.user_id, request.fund_id)

    async def get_funds(self) -> List[FundResponse]:
        # Aquí debes asegurarte de usar await para funciones asincrónicas
        funds = await self.logic.get_funds()
        return [
            {
                "id": fund.get("uuid"),
                "name": fund.get("name"),
                "min_investment": float(fund.get("min_amount")),
                "category": fund.get("category"),
            }
            for fund in funds
        ]
