class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin

    def authenticate(self, user_id, pin):
        return self.user_id == user_id and self.pin == pin


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance


class Transaction:
    def __init__(self):
        self.history = []

    def add_transaction(self, transaction):
        self.history.append(transaction)

    def get_history(self):
        return self.history


class ATM:
    def __init__(self, user, account, transaction):
        self.user = user
        self.account = account
        self.transaction = transaction

    def show_transaction_history(self):
        history = self.transaction.get_history()
        if not history:
            print("No transactions yet.")
        else:
            for h in history:
                print(h)

    def withdraw(self, amount):
        if self.account.withdraw(amount):
            self.transaction.add_transaction(f"Withdraw: {amount}")
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def deposit(self, amount):
        self.account.deposit(amount)
        self.transaction.add_transaction(f"Deposit: {amount}")
        print(f"Deposited: {amount}")

    def transfer(self, amount, other_account):
        if self.account.withdraw(amount):
            other_account.deposit(amount)
            self.transaction.add_transaction(f"Transfer: {amount} to {other_account}")
            print(f"Transferred: {amount} to account {other_account}")
        else:
            print("Insufficient balance")


class Main:
    def __init__(self):
        self.user_db = {"user1": User("user1", "1234")}
        self.account_db = {"user1": Account(1000)}
        self.transaction_db = {"user1": Transaction()}

    def run(self):
        user_id = input("Enter User ID: ")
        pin = input("Enter PIN: ")

        user = self.user_db.get(user_id)
        if not user or not user.authenticate(user_id, pin):
            print("Authentication Failed")
            return

        account = self.account_db.get(user_id)
        transaction = self.transaction_db.get(user_id)
        atm = ATM(user, account, transaction)

        while True:
            print("\n1. Transaction History\n2. Withdraw\n3. Deposit\n4. Transfer\n5. Quit")
            choice = input("Choose an option: ")
            if choice == '1':
                atm.show_transaction_history()
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            elif choice == '3':
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
            elif choice == '4':
                other_user_id = input("Enter recipient User ID: ")
                other_account = self.account_db.get(other_user_id)
                if not other_account:
                    print("Recipient account not found")
                    continue
                amount = float(input("Enter amount to transfer: "))
                atm.transfer(amount, other_account)
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid option, please try again.")


if __name__ == "__main__":
    main = Main()
    main.run()


