"""
Description: A class to manage Client.
Author: Karanveer
Date: 13/09/2024
"""

class BankAccount:
    def __init__(self, account_number, client_number, balance = 0.0):
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number

        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        try:
            self.__balance = float(balance)
        except ValueError:
            self.__balance = 0.0

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def client_number(self):
        return self.__client_number
    
    @property
    def balance(self):
        return self.__balance
    
    # Update balance
    def update_balance(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            return
        self.__balance += amount

    # Deposit
    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if amount <= 0:
            formatted_amount = "${:,.2f}".format(amount)
            raise ValueError(f"Deposit amount: {formatted_amount} must be positive.")
        
        self.update_balance(amount)


    # # Withdraw
    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        
        if amount <= 0:
            formatted_amount = "${:,.2f}".format(amount)
            raise ValueError(f"Withdraw amount: {formatted_amount} must be positive.")
        
        if amount > self.__balance:
            formatted_amount = "${:,.2f}".format(amount)
            formatted_balance = "${:,.2f}".format(self.__balance)
            raise ValueError(f"Withdraw amount: {formatted_amount} must not exceed the account balance: {formatted_balance}.")
        
        self.update_balance(-amount)

    def __str__(self):
        formatted_balance = "${:,.2f}".format(self.__balance)
        return f"Account Number: {self.__account_number} Balance: {formatted_balance}"