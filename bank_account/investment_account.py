"""
Description: A class to manage InvestmentAccount.
Author: Karanveer
"""

from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class InvestmentAccount(BankAccount):
    TEN_YEARS_AGO = date.today() - timedelta(days=10*365.25)

    def __init__(self, account_number, balance, management_fee, date_created):
        super().__init__(account_number, balance)
        self.__management_fee = self._validate_float(management_fee, 2.55)
        self.__date_created = date_created

    def __str__(self):
        if self.__date_created <= InvestmentAccount.TEN_YEARS_AGO:
            management_fee_str = "Waived"
        else:
            management_fee_str = f"${self.__management_fee:.2f}"
        return f"Account Number: {self.get_account_number()}\n" \
               f"Balance: {self.get_balance():.2f}\n" \
               f"Date Created: {self.__date_created}\n" \
               f"Management Fee: {management_fee_str}\n" \
               f"Account Type: Investment"

    def get_service_charges(self):
        if self.__date_created <= InvestmentAccount.TEN_YEARS_AGO:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return BankAccount.BASE_SERVICE_CHARGE + self.__management_fee

    def _validate_float(self, value, default):
        try:
            return float(value)
        except ValueError:
            return default
