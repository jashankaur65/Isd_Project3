"""
Description: A class to manage SavingsAccount.
Author: Karanveer
"""

from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    SERVICE_CHARGE_PREMIUM = 2.00
    MINIMUM_BALANCE_DEFAULT = 50.00

    def __init__(self, account_number, balance, minimum_balance):
        super().__init__(account_number, balance)
        self.__minimum_balance = self._validate_float(minimum_balance, SavingsAccount.MINIMUM_BALANCE_DEFAULT)

    def __str__(self):
        return f"Account Number: {self.get_account_number()}\n" \
               f"Balance: {self.get_balance():.2f}\n" \
               f"Minimum Balance: ${self.__minimum_balance:.2f}\n" \
               f"Account Type: Savings"

    def get_service_charges(self):
        if self.get_balance() >= self.__minimum_balance:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return BankAccount.BASE_SERVICE_CHARGE * SavingsAccount.SERVICE_CHARGE_PREMIUM

    def _validate_float(self, value, default):
        try:
            return float(value)
        except ValueError:
            return default