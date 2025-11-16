class BankAccount:
    def __init__(self, balance=0):
        self.balance=balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully.")
        print(f"Current Balance: ₹{self.balance}\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance! Withdrawal Failed.\n")
        else:
            self.balance -= amount
            print(f"{amount} withdrawal successfully.")
            print(f"Current Balance: ₹{self.balance}\n")

# Main Program
account = BankAccount()
while True:
    print("\n---- Simple Bank Menu ----")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)
    elif choice == 2:
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)
    elif choice == 3:
        print(f"Your Current Balance is: {account.balance}\n")
    elif choice == 4:
        print("Thank you for using the bank system!")
        break
    else:
        print("Invalid Choice! Please tryagain.\n")