from abc import ABC, abstractmethod
from datetime import datetime

class Transaction(ABC):
    @abstractmethod
    def create_account(self, account):
        pass

class Deposit(Transaction):
    def __init__(self, amount):
        self.amount = amount
        self.timestamp = datetime.now()
    
    def create_account(self, account):
        account.deposit(self.amount)
        account.add_transaction(self)

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - Deposited R$ {self.amount}"

class Withdrawal(Transaction):
    def __init__(self, amount):
        self.amount = amount
        self.timestamp = datetime.now()
    
    def create_account(self, account):
        account.withdraw(self.amount)
        account.add_transaction(self)

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - Withdrew R$ {self.amount}"

class Client:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def do_transaction(self, account, transaction):
        transaction.create_account(account)

    def add_account(self, account):
        self.accounts.append(account)

    def list_accounts(self):
        return self.accounts

class PhysicalPerson(Client):
    def __init__(self, cpf, name, birthdate, address):
        super().__init__(address)
        self.cpf = cpf
        self.name = name
        self.birthdate = birthdate

    def __str__(self):
        return f"Name: {self.name}, CPF: {self.cpf}, Address: {self.address}"

class Account:
    def __init__(self, number, client, agency="0001"):
        self.balance = 0
        self.number = number
        self.agency = agency
        self.client = client
        self.__history = []

    def balance(self):
        return self.balance

    def new_account(self, client, number):
        return Account(number, client)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False

    def deposit(self, amount):
        self.balance += amount
        return True

    def add_transaction(self, transaction):
        self.__history.append(transaction)

    def get_history(self):
        return self.__history

class CurrentAccount(Account):
    def __init__(self, number, client, withdraw_limit, withdrawals_limit):
        super().__init__(number, client)
        self.withdraw_limit = withdraw_limit
        self.withdrawals_limit = withdrawals_limit

def display_menu():
    print("\n1. Create User")
    print("2. Create Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Statements")
    print("6. List Users")
    print("7. Exit")

def main():
    users = []

    while True:
        display_menu()
        option = input("Choose an option: ")

        if option == "1":
            name = input("Enter user's name: ")
            cpf = input("Enter user's CPF: ")
            birth_date = input("Enter user's birth date (YYYY-MM-DD): ")
            address = input("Enter user's address: ")

            user = PhysicalPerson(cpf, name, birth_date, address)
            users.append(user)
            print("User created successfully.")

        elif option == "2":
            cpf = input("Enter user's CPF: ")
            found_user = None
            for user in users:
                if user.cpf == cpf:
                    found_user = user
                    break
            if found_user:
                number = input("Enter account's number: ")
                account = Account(number, found_user)
                found_user.add_account(account)
                print("Account created successfully.")
            else:
                print("User not found.")

        elif option == "3":
            cpf = input("Enter user's CPF: ")
            account_number = input("Enter account number: ")
            amount = float(input("Enter the amount to deposit: "))

            found_user = None
            for user in users:
                if user.cpf == cpf:
                    for account in user.accounts:
                        if account.number == account_number:
                            transaction = Deposit(amount)
                            user.do_transaction(account, transaction)
                            print("Deposit successful.")
                            break
                    break

        elif option == "4":
            cpf = input("Enter user's CPF: ")
            account_number = input("Enter account number: ")
            amount = float(input("Enter the amount to withdraw: "))

            found_user = None
            for user in users:
                if user.cpf == cpf:
                    for account in user.accounts:
                        if account.number == account_number:
                            if account.withdraw(amount):
                                transaction = Withdrawal(amount)
                                user.do_transaction(account, transaction)
                                print("Withdrawal successful.")
                            break
                    break

        elif option == "5":
            cpf = input("Enter user's CPF: ")
            account_number = input("Enter account number: ")

            found_user = None
            for user in users:
                if user.cpf == cpf:
                    for account in user.accounts:
                        if account.number == account_number:
                            print(f"Account balance: {account.balance}")
                            print("Transaction history:")
                            for transaction in account.get_history():
                                print(transaction)
                            break
                    break

        elif option == "6":
            print("\nUsers:")
            for user in users:
                print(user)

        elif option == "7":
            print("Exiting the system...")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
