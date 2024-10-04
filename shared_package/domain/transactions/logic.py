from shared_package.domain.transactions.repositories import TransactionRepository

class TransactionLogic:
    def __init__(self):
        self.repository = TransactionRepository()

    async def get_transactions(self):
        transactions = await self.repository.get_user_transactions()
        if not transactions:
            return "No se encontraron transacciones para este usuario."
        return transactions
