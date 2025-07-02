from bank_account.bank_account import BankAccount
from datetime import date
from patterns.observer.subject import Subject  # Adjust this import path as needed

class ChequingAccount(BankAccount, Subject):
    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number: int, client_number: int, balance: float = 0.0, 
                 date_created: date = None, overdraft_limit: float = -100.0, overdraft_rate: float = 0.05):
        if date_created is not None and not isinstance(date_created, date):
            raise ValueError("Date created must be an instance of datetime.date")
        
        BankAccount.__init__(self, account_number, client_number, balance, date_created)
        Subject.__init__(self)  # Initialize the observer list
        
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self.__overdraft_limit = -100.0

        try:
            self.__overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self.__overdraft_rate = 0.05

    def get_service_charges(self):
        if self.balance >= self.__overdraft_limit:
            return ChequingAccount.BASE_SERVICE_CHARGE
        else:
            overdraft_penalty = (self.__overdraft_limit - self.balance) * self.__overdraft_rate
            return ChequingAccount.BASE_SERVICE_CHARGE + overdraft_penalty

    def deposit(self, amount):
        super().deposit(amount)
        self.notify(f"Deposit of {self.format_currency(amount)} made. New balance: {self.format_currency(self.balance)}")

    def withdraw(self, amount):
        super().withdraw(amount)
        self.notify(f"Withdrawal of {self.format_currency(amount)} made. New balance: {self.format_currency(self.balance)}")

    def __str__(self):
        return (f"Account Number: {self.account_number} Balance: {self.format_currency(self.balance)}\n"
                f"Overdraft Limit: {self.format_currency(self.__overdraft_limit)} Overdraft Rate: {self.__overdraft_rate * 100:.2f}% Account Type: Chequing")
