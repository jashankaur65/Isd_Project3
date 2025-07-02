from bank_account.bank_account import BankAccount
from datetime import date, timedelta
from patterns.observer.subject import Subject  # Adjust import path as needed

class InvestmentAccount(BankAccount, Subject):
    TEN_YEARS_AGO = date.today() - timedelta(days=int(10 * 365.25))

    def __init__(self, account_number: int, client_number: int, balance: float = 0.0, 
                 management_fee: float = 2.55, date_created: date = None):
        BankAccount.__init__(self, account_number, client_number, balance, date_created)
        Subject.__init__(self)

        try:
            self.__management_fee = float(management_fee)
        except (ValueError, TypeError):
            self.__management_fee = 2.55

    def get_service_charges(self):
        if self.date_created < InvestmentAccount.TEN_YEARS_AGO:
            # Management fee waived for accounts older than 10 years
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return BankAccount.BASE_SERVICE_CHARGE + self.__management_fee

    def deposit(self, amount):
        super().deposit(amount)
        self.notify(f"Deposit of {self.format_currency(amount)} made. New balance: {self.format_currency(self.balance)}")

    def withdraw(self, amount):
        super().withdraw(amount)
        self.notify(f"Withdrawal of {self.format_currency(amount)} made. New balance: {self.format_currency(self.balance)}")

    def __str__(self):
        management_fee_str = "Waived" if self.date_created < InvestmentAccount.TEN_YEARS_AGO else self.format_currency(self.__management_fee)
        return (f"Account Number: {self.account_number}\n"
                f"Balance: {self.format_currency(self.balance)}\n"
                f"Date Created: {self.date_created}\n"
                f"Management Fee: {management_fee_str}\n"
                f"Account Type: Investment")
