from shared_package.domain.funds.logic import FundLogic
from schemas import SubscribeRequest, CancelSubscriptionRequest, FundResponse
from typing import List


class FundService:
    def __init__(self):
        self.logic = FundLogic()

    async def subscribe(self, request: SubscribeRequest) -> str:
        return self.logic.subscribe_to_fund(
            user_id=request.user_id, fund_id=request.fund_id, amount=request.amount
        )

    async def cancel_subscription(self, request: CancelSubscriptionRequest) -> str:
        return self.logic.cancel_subscription(request.user_id, request.fund_id)

    async def get_funds(self) -> List[FundResponse]:
        funds = self.logic.repository.get_funds()
        return [
            # FundResponse(
            #     id=fund.get("uuid"),
            #     name=fund.get("name"),
            #     min_investment=float(fund.get("min_amount")),
            #     category=fund.get("category"),
            # )
            {
                "id":fund.get("uuid"),
                "name": fund.get("name"),
                "min_investment": float(fund.get("min_amount")),
                "category": fund.get("category"),
            }
            for fund in funds
        ]
