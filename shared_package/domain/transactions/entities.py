from datetime import datetime
import uuid

class Transaction:
    def __init__(self, user_id: int, fund_name: str, amount: float, transaction_type: str, timestamp: datetime):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.fund_name = fund_name
        self.amount = amount
        self.transaction_type = transaction_type  # 'subscription' or 'cancellation'
        self.timestamp = timestamp
