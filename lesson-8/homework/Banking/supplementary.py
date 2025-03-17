from uuid import uuid4


class Account:
    """Represents a bank account with an account number, name, and balance."""

    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = float(balance)  # Ensure balance is stored as a float

    def __str__(self):
        """Returns a string representation of the account details."""
        return f"{self.account_number} {self.name} {self.balance:.2f}"


def generate_account_number():
    """Generates a unique 12-digit account number."""
    return str(uuid4().int)[:12]


def show_menu():
    """Displays the banking system menu."""
    print("""
    1. Create a new account
    2. View account
    3. Deposit
    4. Withdraw
    5. Save to a file
    6. Exit
    """)


class Bank:
    """Manages multiple accounts with functionalities like deposit, withdraw, and file saving."""

    def __init__(self):
        self.accounts = {}  # {account_number: Account object}
        self.load_from_file("accounts_info.txt")

    def rep(self):
        """Returns all accounts in a formatted string."""
        return '\n'.join(str(acc) for acc in self.accounts.values())

    def create_account(self, account_number, name, balance):
        """Creates a new account if the account number doesn't already exist."""
        if account_number in self.accounts:
            print("Account already exists.")
            return
        self.accounts[account_number] = Account(account_number, name, balance)
        print("Account created successfully!")
        print(self.accounts[account_number])

    def view_account(self, account_number):
        """Displays account details if the account exists."""
        if account_number in self.accounts:
            print(self.accounts[account_number])
        else:
            print("Account doesn't exist.")

    def deposit(self, account_number, amount):
        """Deposits a valid amount into an account."""
        if account_number not in self.accounts:
            print("Account doesn't exist.")
            return
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.accounts[account_number].balance += amount
        print(f"Amount deposited successfully! New balance: {self.accounts[account_number].balance:.2f}")

    def withdraw(self, account_number, amount):
        """Withdraws a valid amount if sufficient balance is available."""
        if account_number not in self.accounts:
            print("Account doesn't exist.")
            return
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.accounts[account_number].balance < amount:
            print("Insufficient funds!")
            return
        self.accounts[account_number].balance -= amount
        print(f"Amount withdrawn successfully! New balance: {self.accounts[account_number].balance:.2f}")

    def save_to_file(self, path="accounts_info.txt"):
        """Saves all account details to a file."""
        try:
            with open(path, 'w') as f:
                f.write(self.rep() + '\n')
            print("Account info saved to file successfully!")
        except Exception as e:
            print(f"Error occurred while saving: {e}")

    def handle_input(self):
        """Handles user input for creating an account."""
        name = input("Enter your name: ").strip()
        while True:
            try:
                amount = float(input("Enter your initial deposit: "))
                if amount < 0:
                    print("Initial deposit cannot be negative.")
                else:
                    break
            except ValueError:
                print("Invalid amount. Please enter a valid number.")

        account_number = generate_account_number()
        self.create_account(account_number, name, amount)

    def interact(self):
        """Handles user interaction with the banking system."""
        while True:
            show_menu()
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.handle_input()
                elif choice == 2:
                    account_number = input("Enter your account number: ").strip()
                    self.view_account(account_number)
                elif choice == 3:
                    account_number = input("Enter your account number: ").strip()
                    try:
                        amount = float(input("Enter deposit amount: "))
                        self.deposit(account_number, amount)
                    except ValueError:
                        print("Invalid amount. Please enter a valid number.")
                elif choice == 4:
                    account_number = input("Enter your account number: ").strip()
                    try:
                        amount = float(input("Enter withdrawal amount: "))
                        self.withdraw(account_number, amount)
                    except ValueError:
                        print("Invalid amount. Please enter a valid number.")
                elif choice == 5:
                    self.save_to_file()
                elif choice == 6:
                    print("Exiting banking system. Goodbye!")
                    break
                else:
                    print("Invalid option. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def load_from_file(self, path="accounts_info.txt"):
        """Loads account details from a file if it exists."""
        try:
            with open(path, 'r') as f:
                for line in f:
                    data = line.strip().split()
                    if len(data) == 3 and data[0] not in self.accounts:
                        account_number, name, balance = data
                        try:
                            balance = float(balance)
                            if balance >= 0:
                                self.accounts[account_number] = Account(account_number, name, balance)
                        except ValueError:
                            pass  # Ignore invalid balance values
        except FileNotFoundError:
            pass  # No file means no accounts exist yet
