from datetime import date
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class BankAccount:
    BASE_SERVICE_CHARGE = 5.00

    def __init__(self, account_number: int, client_number: int, balance=0.0, date_created: date = None, strategy: ServiceChargeStrategy = None):
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number

        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        try:
            self.__balance = float(balance)
        except (ValueError, TypeError):
            # On invalid balance string, default to 0.0 as test expects
            self.__balance = 0.0

        if date_created is None:
            self.__date_created = date.today()
        elif isinstance(date_created, date):
            self.__date_created = date_created
        else:
            raise ValueError("Date created must be an instance of datetime.date")

        self.strategy = strategy

    @property
    def account_number(self):
        return self.__account_number

    @property
    def client_number(self):
        return self.__client_number

    @property
    def balance(self):
        return self.__balance

    @property
    def date_created(self):
        return self.__date_created

    def update_balance(self, amount):
        try:
            amount = float(amount)
            self.__balance += amount
        except (ValueError, TypeError):
            # Ignore invalid amounts, leave balance unchanged (matches test)
            pass

    def deposit(self, amount):
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Deposit amount: {self.format_currency(amount)} must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Withdraw amount: {self.format_currency(amount)} must be positive.")
        if amount > self.__balance:
            raise ValueError(f"Withdraw amount: {self.format_currency(amount)} must not exceed the account balance: {self.format_currency(self.__balance)}.")
        self.update_balance(-amount)

    def get_service_charges(self):
        if self.strategy:
            return self.strategy.calculate_service_charges(self)
        return self.BASE_SERVICE_CHARGE

    @staticmethod
    def format_currency(amount):
        return "${:,.2f}".format(amount)

    def __str__(self):
        # Match the test expectation exactly
        return f"Account Number: {self.__account_number} Balance: {self.format_currency(self.__balance)}"
