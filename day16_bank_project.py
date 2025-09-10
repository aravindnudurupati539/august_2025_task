class bank_account():
    def __init__(self, username, password, balance=0,):
        self.username = username
        self.password = password
        self.balance = balance
    def deposit(self,amount):
        if amount <= 0:
            return("please enter postive amount.")
        self.balance +=amount
        return (f"Amount deposit : {amount}, Total balance : {self.balance}")
    def withdraw(self,amount):
        if amount <= 0:
            return "please enter postive amount."
        if amount > self.balance:
            return ("Insufficient balance.")
        self.balance -=amount
        return(f"withdraw {amount} from your account and remaining balance {self.balance}")
    def check_balance(self):
        return (f"Your current balance is: {self.balance}")
    def get_mini_statement(self):
        yield("Mini statement:")
        yield(f"Username: {self.username}")
        yield(f"Current balance: {self.balance}")
        pass
    pass

class BankingSystem:
    def __init__(self):
        self.accounts = {}
# the BankingSystem class is defined. It has one instance variable - accounts - which is a dictionary that stores the username as key and the Account object as value.

    def create_account(self, username, password,account):
        if username in self.accounts:
            print("Username already exists")
        else:
            self.accounts[username] = Account(username, password)
            print("\nAccount created successfully")
            print("-------Welcome to PYTHON Bank-------")

# The create_account method takes two arguments - username and password. It checks if the username already exists in the accounts dictionary. If it does, it prints a message saying that the username already exists. If it does not, it creates a new Account object with the given username and password and adds it to the accounts dictionary. It then prints a message saying that the account was created successfully.

    def login(self, username, password):
        if username in self.accounts:
            account = self.accounts[username]
            if account.password == password:
                print("Login Sucess....")
                return account
            else:
                print("Invalid password")
        elif account_number in self.accounts:
        
        else:
            print("Invalid username")
        return None


bank = bank_account()
while True:
    print("\n")
    print("1. Create account")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        bank.create_account(username, password)
    elif choice == '2':
        pass
    elif choice == '3':
        pass

