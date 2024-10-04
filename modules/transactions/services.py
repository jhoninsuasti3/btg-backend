from shared_package.domain.transactions.logic import TransactionLogic


class TransactionService:
    def __init__(self):
        self.logic = TransactionLogic()

    async def get_transactions(self):
        return await self.logic.get_transactions()
