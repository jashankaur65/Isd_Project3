from bank_account.bank_account import BankAccount
from datetime import date
from patterns.observer.subject import Subject  # Adjust the import path if needed

class SavingsAccount(BankAccount, Subject):
    SERVICE_CHARGE_PREMIUM = 2.00
    MINIMUM_BALANCE_DEFAULT = 50.00

    def __init__(self, account_number: int, client_number: int, balance: float = 0.0, 
                 minimum_balance: float = MINIMUM_BALANCE_DEFAULT, date_created: date = None):
        BankAccount.__init__(self, account_number, client_number, balance, date_created)
        Subject.__init__(self)

        try:
            self.__minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.__minimum_balance = SavingsAccount.MINIMUM_BALANCE_DEFAULT

    def get_service_charges(self):
        if self.balance >= self.__minimum_balance:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return BankAccount.BASE_SERVICE_CHARGE * SavingsAccount.SERVICE_CHARGE_PREMIUM

    def deposit(self, amount):
        super().deposit(amount)
        self.notify(f"Deposit of {self.format_currency(amount)} made. New balance: {self.format_currency(self.balance)}")

    def withdraw(self, amount):
        super().withdraw(amount)
        self.notify(f"Withdrawal of {self.format_currency(amount)} made. New balance: {self.format_currency(self.balance)}")

    @property
    def minimum_balance(self):
        return self.__minimum_balance

    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Balance: {self.format_currency(self.balance)}\n"
                f"Minimum Balance: {self.format_currency(self.__minimum_balance)}\n"
                f"Account Type: Savings")
