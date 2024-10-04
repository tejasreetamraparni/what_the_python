"""
Different operations that can be performed within the program
"""

def current_balance(account):
    """
    Calculate balance with overdraft and interest

    --
    Savings:
    Interest: Principal * Rate of interest * Time period
    Dummy values for time period = 12 months

    Current:
    Adds account's overdraft limit to balance
    """
    balance = account.balance

    #dummy interest calculation

    if account.account_type == 'savings':
        interest_rate = account.interest_rate
        balance += (balance * interest_rate * 12)
    if account.account_type == 'current':
        od_limit = account.overdraft_limit
        balance += od_limit
    return balance

def show_balance(customer):
    """
    Shows two balances:
    1. Initial balance: Current balance of the account
    2. Final balance: Adds interest or overdraft limit depending on account type
    """
    for account_number, account in customer.accounts.items():
        curr_balance = current_balance(account)
        print(f"Account Number:{account_number}     Account_type:{account.account_type}")
        print(f"Initial Balance: {account.balance}      Final Balance:{curr_balance}")

def deposit(account, amount):
    """
    Deposit specified amount into account
    """
    account.deposit(amount)


def withdraw(account, amount):
    """
    Withdraw specified amount from account
    Sufficient funds are calculated using current_balance module
    as both interest and overdraft limit need to be considered as total available funds

    Returns True if sufficient funds exists else False
    """
    curr_balance = current_balance(account=account)
    if curr_balance >= amount:
        account.withdraw(amount)
        return True
    return False

def transfer(from_account, to_account, amount):
    """
    Transfer amount between accounts
    success: True if sufficient funds exist in sender account
    Deposit happens only when Withdraw is successful
    """
    # Transfer amount from account1 to account2

    success = withdraw(account=from_account, amount=amount)
    if success:
        deposit(to_account, amount=amount)
        print("Transfer Successful!")
    else:
        print("Insufficient funds!\n")
