def showMenu():
    menu = """
    |--------   BANK  --------|
    |-------------------------|
    |  d  - Deposit           |
    |  w  - Withdraw          |
    |  s  - Statements        |
    |  cu - Create user       |
    |  ca - Create account    |
    |  lu - List users        |
    |  la - List accounts     |
    |  e  - Exit              |
    ---------------------------
    """
    return menu

def createUser(userList, cpf):
    for user in userList:
        if user["cpf"] == cpf:
            print("User with the same CPF already exists.")
            return None
    name = input("Enter user's name: ")
    birthDate = input("Enter user's birth date: ")
    lg = input("Enter user's address (logradoura): ")
    nr = input("Enter user's address (numero): ")
    city = input("Enter user's address (city): ")

    user = {"name": name, "cpf": cpf, "birthDate": birthDate, "address": {"lg": lg, "nr": nr, "city": city}, "accounts": []}
    userList.append(user)
    return user

def listUsers(userList):
    print("List of Users:")
    for user in userList:
        print(f"CPF: {user['cpf']}, Name: {user['name']}")

def createAccount(userList, accountsList, cpf):
    user = None
    for u in userList:
        if u["cpf"] == cpf:
            user = u
            break
    if user is None:
        print("User not found.")
        return

    account = {"agency": "0001", "number": len(user["accounts"]) + 1, "cpf": cpf, "balance": 0, "withdrawCount": 0}
    user["accounts"].append(account)
    accountsList.append(account)

def listAccounts(userList, cpf):
    for user in userList:
        if user["cpf"] == cpf:
            print(f"Accounts for user {user['name']} (CPF: {cpf}):")
            for account in user["accounts"]:
                print(f"Agency: {account['agency']}, Number: {account['number']}")
            return
    print("User not found.")

def depositBalance(accountsList, cpf, amount):
    for account in accountsList:
        if account["cpf"] == cpf:
            # Update balance
            account["balance"] = account.get("balance", 0) + amount
            # Update statement
            account["statement"] = account.get("statement", []) + [f"Deposited R$ {amount} to your account."]
            print("Deposit successful.")
            return
    print("Account not found.")

def withdrawBalance(accountsList, cpf, amount):
    for account in accountsList:
        if account["cpf"] == cpf:
            if "balance" not in account:
                print("Insufficient funds. Please deposit money first.")
                return
            if account["balance"] < amount:
                print("Insufficient funds.")
                return
            if account.get("withdrawCount", 0) >= 3:
                print("You have reached the maximum number of withdrawals.")
                return
            if amount > 500:
                print("Withdrawal amount exceeds maximum limit (R$ 500).")
                return
            # Update balance
            account["balance"] -= amount
            # Update statement
            account["statement"] = account.get("statement", []) + [f"Withdrew R$ {amount} from your account."]
            # Update withdrawal count
            account["withdrawCount"] = account.get("withdrawCount", 0) + 1
            print("Withdrawal successful.")
            return
    print("Account not found.")

def getStatement(accountsList, cpf):
    for account in accountsList:
        if account["cpf"] == cpf:
            print(" STATEMENTS ".center(50, "#"))
            for statement in account.get("statement", []):
                print(statement)
            print("***".center(50, "-"))
            return
    print("Account not found.")

def runTheBank():
    userList = []
    accountsList = []

    while True:
        option = input(showMenu())

        if option == "cu":
            cpf = input("Enter user's CPF: ")
            createUser(userList, cpf)

        elif option == "ca":
            cpf = input("Enter user's CPF: ")
            createAccount(userList, accountsList, cpf)

        elif option == "lu":
            listUsers(userList)

        elif option == "la":
            cpf = input("Enter user's CPF: ")
            listAccounts(userList, cpf)

        elif option == "d":
            cpf = input("Enter user's CPF: ")
            amount = float(input("Enter the amount to deposit: "))
            depositBalance(accountsList, cpf, amount)

        elif option == "w":
            cpf = input("Enter user's CPF: ")
            amount = float(input("Enter the amount to withdraw: "))
            withdrawBalance(accountsList, cpf, amount)

        elif option == "s":
            cpf = input("Enter user's CPF: ")
            getStatement(accountsList, cpf)

        elif option == "e":
            print("Exiting the system...")
            break

        else:
            print("Invalid option. Please try again.")


runTheBank()