"""
---------------Bank Management System--------------

Author: Teja Sree Tamraparni

"""

from models import Bank
from methods import show_balance, deposit, withdraw, transfer
from utils import get_customer, get_account, show_accounts

def display_menu():
    """
    This menu will be shown to the user when main() is called
    """
    print("****************WELCOME**********************")
    print("1. Create a new customer")
    print("2. Create a new account")
    print("3. Deposit amount")
    print("4. Withdraw amount")
    print("5. Transfer amount")
    print("6. Show customer balance")
    print("7. Delete account")
    print("8. Exit")

#Create a new Bank instance
bank = Bank()

def main():
    """
    Entry point for the program
    """
    #Run the loop until choice="No"
    choice = "Yes"

    while choice == "Yes":

        display_menu()
        option = int(input("Choose your option:"))

        #User chooses an option
        if option == 1:
            print("Creating new customer....")
            name = input("Enter your name:")
            customer_id, account_number = bank.create_customer(name)
            print("Customer created!")
            print(f"Customer ID:{customer_id}")
            print(f"Default account number:{account_number}")

        elif option == 2:
            print("Creating a new account...")
            customer_id = int(input("Enter your customer_id:"))

            #Fetch customer details
            customer = get_customer(customer_id, bank=bank)
            #Create a new account
            account_type = input("Enter account type (savings/current):")
            account_number = customer.create_account(account_type)
            print(f"{account_type.upper()} account created!")
            print(f"Account number is:{account_number}")

        elif option == 3:
            print("Depositing amount....")
            customer_id = int(input("Enter your customer_id:"))

            #Fetch customer details
            customer = get_customer(customer_id, bank=bank)
            print("Showing account...")
            show_accounts(customer=customer)
            account_number = int(input("In which account do you want to deposit the amount?:"))
            amount = int(input("Enter the amount to deposit (1000-9999):"))
            #Fetch account details
            account = get_account(account_number=account_number, customer=customer)

            #If account exists, proceed to deposit and show balance
            if account:
                deposit(account=account, amount=amount)
                show_balance(customer)
            else:
                print("Error! Invalid account number.")

        elif option == 4:
            print("Withdrawing amount...")
            customer_id = int(input("Enter your customer_id:"))

            #Fetch customer details
            customer = get_customer(customer_id, bank=bank)       
            print("Showing accounts...")
            show_accounts(customer)
            account_number = int(input("From which account do you want to withdraw the amount?:"))
            amount = int(input("Enter the amount to withdraw (1000-9999):"))

            #Fetch account details
            account = get_account(account_number=account_number, customer=customer)

            #If account exists, proceed to withdraw
            if account:
                success = withdraw(account=account, amount=amount)

                #Withdraw takes place only if account has sufficient funds
                #Check if Withdraw action returned True
                if success:
                    show_balance(customer)
                else:
                    print("Insufficient Funds!")
            else:
                print("Error! Invalid account number.\n")

        elif option == 5:
            print("Transferring money....")

            from_customer_id = int(input("Enter the sender's customer_id:"))
            sender = get_customer(customer_id=from_customer_id, bank=bank)

            print("Showing accounts...")
            show_accounts(customer=customer)

            from_account_number = int(input("Select the sender's account:"))
            amount = int(input("Enter the amount to send:"))
            from_account = get_account(from_account_number, customer=sender)

            to_customer_id = int(input("Enter the receiver's customer_id:"))
            receiver = get_customer(customer_id=to_customer_id, bank=bank)

            print("Showing accounts...")
            show_accounts(customer=customer)

            to_account_number = int(input("Select the receiver's account:"))
            to_account = get_account(account_number=to_account_number, customer=receiver)

            #Check if both sender and receiver accounts exists
            #Check if not transferring to same account

            if (from_account and to_account) and (from_account != to_account):
                transfer(from_account=from_account, to_account=to_account, amount=amount)
            else:
                print("Error! Check that the right accounts are specified.")
            

        elif option == 6:
            print("Showing customer balance...")
            customer_id = int(input("Enter customer_id:"))
            customer = get_customer(customer_id=customer_id, bank=bank)
            print("List of accounts for Customer:")
            show_balance(customer)

        elif option == 7:
            print("Deleting customer account....")
            customer_id = int(input("Enter customer_id:"))
            customer = get_customer(customer_id=customer_id, bank=bank)

            print("Showing accounts...")
            show_accounts(customer=customer)

            #Delete if account exists

            account_number = int(input("Which account would you like to delete?:"))
            account = get_account(account_number=account_number, customer=customer)
            print("\n")
            print("**************************************WARNING*************************************************")
            print("Accounts deleted once cannot be recovered! Any existing balance will be confiscated by bank!\n")
            print("To avoid losing money, transfer the amount to another account first!\n")
            proceed = input("       Would you like to proceed with deletion? (Yes/No):      ")
            if proceed == "Yes":
                if account:
                    customer.accounts.pop(account_number)
                    print("\nAccount Deleted!\n")
                else:
                    print("Invalid Account!\n")
            else:
                print("Wise Decision! Come back when you're ready!\n")

        elif option == 8:
            print(".......................Exiting........................")
            print("=========================GOODBYE=====================")
            break

        else:
            print("Invalid option...")

        print("==================END OF TRANSACTION=====================")
        print("\n")
        choice = input("        Do you wish to continue? (Yes/No):      ")
        print("\n")
        if choice == "No":
            print("=========================GOODBYE=====================")
            break

if __name__ == "__main__":
    main()
