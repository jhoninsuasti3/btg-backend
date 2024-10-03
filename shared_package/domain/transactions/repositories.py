from typing import List
from .entities import Transaction


class TransactionRepository:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def get_user_transactions(self, user_id: int) -> List[Transaction]:
        return [txn for txn in self.transactions if txn.user_id == user_id]
