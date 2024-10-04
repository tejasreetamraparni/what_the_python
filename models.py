class Bank:
    """
    Creates a new bank object. Banks contain customers.
    """
    def __init__(self):
        self.customers = {}
    
    def create_customer(self, name):
        """
        Create a new customer and add to dict
        of customers
        """
        customer_id = len(self.customers.keys()) + 1
        customer = Customer(name=name, customer_id=customer_id)
        self.customers[customer_id] = customer
        # create first default account
        account_number = customer.create_account("savings")
        return customer.customer_id, account_number
    
class Customer:
    """
    Represents a customer. Customers can hold many accounts.
    --
    Attributes:
    name : customer name
    customer_id : unique id, generating by class automatically
    accounts : dict object; key:acc_number, val:account object
    """
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = {}

    def create_account(self, account_type):
        """
        Create an account to perform functions
        such as deposit, withdraw, check_balance
        """
        account_number = len(self.accounts) + 1
        if account_type == "savings":
            account = SavingsAccount(account_number)
        if account_type == "current":
            account = CurrentAccount(account_number)
        self.accounts[account_number] = account
        return account_number
    
    def delete_account(self, account_number):
        """
        Deletes an account if it exists
        """
        try:
            account = self.accounts[account_number]
            if account:
                return self.accounts.pop(account_number)
        except KeyError:
            print("No such account exists.")

class Account:
    """
    Create an account for customer
    """
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance= balance
    
    def check_balance(self):
        """
        Returns account balance
        """
        return self.balance
    
    def deposit(self, amount):
        """
        Add amount to current balance
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Subtract amount from current balance
        """
        self.balance -= amount


class SavingsAccount(Account):
    """
    Type of account that provides interest
    Default account when creating a new customer
    """
    account_type = "savings"
    def __init__(self, account_number, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

class CurrentAccount(Account):
    """
    Type of account that can be overdrawn upto a limit
    """
    account_type = "current"
    def __init__(self, account_number, balance=0.0, overdraft_limit=1000):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit