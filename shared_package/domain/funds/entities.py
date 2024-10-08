from datetime import datetime
import uuid


class Fund:
    def __init__(self, id: int, name: str, category: str, min_investment: float):
        self.id = id
        self.name = name
        self.category = category
        self.min_investment = min_investment


class Subscription:
    def __init__(
        self, user_id: int, fund: Fund, amount: float, subscribed_at: datetime
    ):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.fund = fund
        self.amount = amount
        self.subscribed_at = subscribed_at

    def __str__(self) -> str:
        return (
            f"Subscription with id={self.id}, user_id={self.user_id}, "
            f"fund={self.fund.name}, amount={self.amount}, "
            f"subscribed_at={self.subscribed_at.isoformat()}"
        )
