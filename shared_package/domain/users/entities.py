import uuid


class User:
    def __init__(self, email: str, balance: float):
        self.id = str(uuid.uuid4())
        self.email = email
        self.balance = balance

    def __str__(self) -> str:
        return f"User with id={self.id}, email={self.email}," f"fund={self.balance}"
