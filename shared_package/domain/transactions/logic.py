from .entities import Transaction
from .repositories import TransactionRepository
from domain.funds.repositories import FundRepository
from typing import List
from datetime import datetime


class TransactionLogic:
    def __init__(self):
        self.transaction_repository = TransactionRepository()
        self.fund_repository = FundRepository()

    def record_subscription(self, user_id: int, fund_id: int, amount: float):
        fund = next((f for f in self.fund_repository.funds if f.id == fund_id), None)
        if fund:
            transaction = Transaction(
                user_id=user_id,
                fund_name=fund.name,
                amount=amount,
                transaction_type="subscription",
                timestamp=datetime.now(),
            )
            self.transaction_repository.add_transaction(transaction)

    def record_cancellation(self, user_id: int, fund_id: int):
        fund = next((f for f in self.fund_repository.funds if f.id == fund_id), None)
        if fund:
            transaction = Transaction(
                user_id=user_id,
                fund_name=fund.name,
                amount=0,  # amount is not applicable for cancellations
                transaction_type="cancellation",
                timestamp=datetime.now(),
            )
            self.transaction_repository.add_transaction(transaction)

    def get_transaction_history(self, user_id: int) -> List[Transaction]:
        return self.transaction_repository.get_user_transactions(user_id)
