from domain.transactions.logic import TransactionLogic
from .schemas import TransactionHistoryResponse


class TransactionService:
    def __init__(self):
        self.logic = TransactionLogic()

    async def get_transaction_history(self, user_id: int) -> TransactionHistoryResponse:
        transactions = self.logic.get_transaction_history(user_id)
        return TransactionHistoryResponse(transactions=transactions)
