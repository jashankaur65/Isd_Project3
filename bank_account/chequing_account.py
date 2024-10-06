"""
Description: A class to manage ChequingAccount.
Author: Karanveer
"""

from bank_account.bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
    BASE_SERVICE_CHARGE = 0.50

    def _init_(self, account_number : int, client_number : int, balance = 0.0, date_created = date, overdraft_limit = float, overdraft_rate = float):
        super()._init_(account_number, client_number, balance, date_created)

        try:
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError:
            self.__overdraft_limit = -100.0

        try:
            self.__overdraft_rate = float(overdraft_limit)
        except ValueError:
            self.__overdraft_rate = 0.05
    
    def _str_(self):
        account_status = super()._str_()

        overdraft_status = (f"Overdraft Limit: ${self.__overdraft_limit:,.2f} Overdraft Rate:{self.__overdraft_rate*100:.2f}% Account type: Chequing")

        return f"{account_status}\n{overdraft_status}"
    
    def get_service_charges(self):
        if self.balance >= self._overdraft_limit:
            return ChequingAccount.BASE_SERVICE_CHARGE
        else:
            overdraft_penalty =(self.__overdraft_limit - self.balance) * self.__overdraft_rate
            return ChequingAccount.BASE_SERVICE_CHARGE + overdraft_penalty