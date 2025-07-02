"""
A03_main.py
Demonstrates the Observer Pattern with various BankAccount types.
"""

from datetime import date
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from client.client import Client

# 1. Create Client 1
client1 = Client(1001, "Alice", "Smith", "alice.smith@example.com")

# 2. Create Chequing and Savings accounts for Client 1
chequing_account = ChequingAccount(2001, client1.client_number, 1000.00)
savings_account = SavingsAccount(2002, client1.client_number, 2000.00, 50.00)

# 3. Attach Client 1 as an observer to both accounts
chequing_account.attach(client1)
savings_account.attach(client1)

# 4. Create Client 2 and a SavingsAccount
client2 = Client(1002, "Bob", "Jones", "bob.jones@example.com")
savings_account2 = SavingsAccount(2003, client2.client_number, 2000.00, 50.00)
savings_account2.attach(client2)

# 5. Perform Transactions on ChequingAccount
print("\n--- Transactions on ChequingAccount ---")
try:
    chequing_account.deposit(500.00)
    print("Deposit of $500 completed.")
except Exception as e:
    print(f"Error during deposit: {e}")

try:
    chequing_account.withdraw(100.00)
    print("Withdrawal of $100 completed.")
except Exception as e:
    print(f"Error during withdrawal: {e}")

try:
    chequing_account.withdraw(2000.00)
    print("Withdrawal of $2000 completed.")
except Exception as e:
    print(f"Error during withdrawal: {e}")

# 6. Perform Transactions on SavingsAccount
print("\n--- Transactions on SavingsAccount ---")
try:
    savings_account.withdraw(500.00)
    print("Withdrawal of $500 completed.")
except Exception as e:
    print(f"Error during withdrawal: {e}")

try:
    savings_account.deposit(200.00)
    print("Deposit of $200 completed.")
except Exception as e:
    print(f"Error during deposit: {e}")

try:
    savings_account.withdraw(10000.00)
    print("Withdrawal of $10000 completed.")
except Exception as e:
    print(f"Error during withdrawal: {e}")

# 7. Perform Transactions on SavingsAccount 2 (Bob’s account)
print("\n--- Transactions on Bob's SavingsAccount ---")
try:
    savings_account2.deposit(300.00)
    print("Deposit of $300 completed.")
except Exception as e:
    print(f"Error during deposit: {e}")

try:
    savings_account2.withdraw(100.00)
    print("Withdrawal of $100 completed.")
except Exception as e:
    print(f"Error during withdrawal: {e}")

try:
    savings_account2.withdraw(5000.00)
    print("Withdrawal of $5000 completed.")
except Exception as e:
    print(f"Error during withdrawal: {e}")
