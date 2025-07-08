from dataclasses import dataclass

# ✅ First dataclass for basic user info
@dataclass
class User:
    username: str
    password: str
    account_number: str
    balance: float

# ✅ Create a User object
account1 = User("Farhana Yousuf", "Farhana123", "1234567890", 10000.0)

# ✅ Also showing dictionary style for comparison
account_dict = {
    'username': 'Farhana Yousuf',
    'password': 'Farhana123',
    'account_number': '1234567890',
    'balance': 10000.0,
}

print("Welcome to the ATM")
print("Please enter your username and password to access your account.")

# ✅ Second dataclass for deposit method
@dataclass
class Account:
    name: str
    account_number: int
    balance: float = 0.0  # Default balance value

    def deposit(self, amount: float):
        self.balance += amount
        print(f"Depositing {amount}")

# ✅ Creating an Account object
farhana = Account("Farhana Yousuf", 1234567890, 10000.0)

# ✅ Making a deposit
farhana.deposit(1000)

# ✅ Printing updated balance
print(f"Current Balance: {farhana.balance}")
