class BankAccount():
    def __init__(self, holder: str, amount: int = 0) -> None:
        self.holder = holder
        self.balance = amount

    def deposit(self, amount: int) -> None:
        self.balance += amount
        print(f"Success: {amount} deposited to account")
    
    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            print("Err: Insufficient Amount")
        else:
            self.balance -= amount
            print(f"Success: New balance is {self.balance}")
    
    def __str__(self) -> str:
        return f"Bank Account: {self.holder}, {self.balance}"