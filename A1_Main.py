from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    client = Client(101, "Marie", "Curie", "marie.curie@example.com")
    account = BankAccount(50001, 2000.00)

    print(client)
    print(account)
account.deposit(500)
    account.withdraw(300)
    print("After transactions:")
    print(account)

if __name__ == "__main__":
    main()