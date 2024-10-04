def get_customer(customer_id, bank=None):
    """
    Fetch customer object details from given customer_id
    """
    return bank.customers[customer_id]

def get_account(account_number, customer=None):
    """
    Fetch account details from Customer
    If account exists, return account object, else False
    """
    if customer.accounts.get(account_number):
        return customer.accounts[account_number]
    else:
        return False

def show_accounts(customer):
    """
    Display all available accounts for a customer
    """
    for account_number, account in customer.accounts.items():
        print(f"Account Number:{account_number}     Account Type:{account.account_type}")

