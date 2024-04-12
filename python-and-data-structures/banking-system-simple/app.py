### Banking System ###

# Initial amount of money in the account, deposit
balance = 0.0
deposit= 0.0

# Option selected by the user
option = 0
#Counter for the amount of money withdrawn
withdrawCount = 0

# Maximum allowed amount of withdraw & Maximum amount of withdraw
WITHDRAW_TIMES_LIMIT = 3
WITHDRAW_AMOUNT_LIMIT = 500.00

# Statement that will contain the operations to be performed
statement = ""

menu = f"""
*   BANK   *

d - Deposit
w - Withdraw
s - Statements
e - Exit 

"""


while True:

    option = input(menu+f"Your current balance is: R$ {balance}\n")

    ## Deposit
    if option == "d":
        deposit = float(input("Please enter the amount to deposit:\n"))

        if deposit <= 0:
            print("Deposit amount must be greater than zero.\n")
        else:
            balance += deposit
            statement += f"Deposited R$ {deposit} to your account.\n"

    ## Withdraw
    elif option == "w":

        withdraw = float(input("Please enter the amount to withdraw:\n"))
        if withdraw <= balance:
            balance -= withdraw
            statement += f"Withdrew R$ {withdraw} from your account.\n"
            withdrawCount +=1
        else:
            print("Unfortunately you don't have enough balance to withdraw.\n")

        if withdrawCount > WITHDRAW_AMOUNT_LIMIT:
            print(f"You can only withdraw up to R$ {WITHDRAW_AMOUNT_LIMIT} times.\n")

    ## Statements
    elif option == "s":
        print(" STATEMENTS ".center(50, "#"))
        print(statement)
        print("***".center(50, "-"))

    ## Exit
    elif option == "e":
        print("...Exiting the System...")
        break

    ## Invalid option
    else:
        print("Invalid option, please try again!\n")