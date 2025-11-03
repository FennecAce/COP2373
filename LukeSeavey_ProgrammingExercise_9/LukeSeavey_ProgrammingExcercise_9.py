# Bank account class with methods for deposit, withdrawal, interest adjustment, and interest calculation.

class BankAcct:
    
    def __init__(self, name, account_number, amount, interest_rate):
        
        self.name = name
        
        self.account_number = account_number
        
        self.amount = amount 
        
        self.interest_rate = interest_rate # this is a annual rate

    def deposit(self, amount):
        
        if amount > 0:
            
            self.amount += amount
            
            print(f"Deposited: ${amount:.2f}. New balance: ${self.amount:.2f}")
        
        else:
            
            print("Deposit amount must be positive.")


    def withdraw(self, amount):
        
        if 0 < amount <= self.amount:
            
            self.amount -= amount
            
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.amount:.2f}")
        
        else:
            
            print("Insufficient funds or invalid withdrawal amount.")

    
    def adjust_interest(self, new_rate):
        
        if new_rate >= 0:
            
            self.interest_rate = new_rate
            
            print(f"Interest rate adjusted to: {self.interest_rate:.2f}%")
        
        else:
            
            print("Interest rate cannot be negitive.")

    def get_balance(self):
        
        return self.amount
    
    def calculate_interest(self, days):
        
        # Intrest calculation amount for given days.
        
        interest = self.amount * (self.interest_rate / 100) * (days / 365) 
        
        return interest
    
    def __str__(self):
        
        return (f"Account Holder: {self.name}\n"
                
                f"Account Number: {self.account_number}\n"
                
                f"Balance: ${self.amount:.2f}\n"
                
                f"Interest Rate: {self.interest_rate:.2f}%")
    
# Test bed

def test_bank_account():
    
    acct = BankAcct("John Doe", "123456789", 1000.00, 3.5)
    
    print(acct)

    acct.deposit(500)

    acct.withdraw(200)

    acct.adjust_interest(4.0)

    print(f"Current Balance: ${acct.get_balance():.2f}")

    interest_30_days = acct.calculate_interest(30)
    
    print(f"Interest for 30 days: ${interest_30_days:.2f}")

    print("\nFinal Account Details:")
    
    print(acct)

# Main code with fuctions to either run test bed or create a new account.

if __name__ == "__main__":
    
    print("Welcome to Fox bamking service.")
    
    choice = input("Would you like to (1) Run Test Bed or (2) Create New Account? Enter 1 or 2: ")
    
    if choice == '1':
        
        test_bank_account()
    
    elif choice == '2':
        
        name = input("Enter account holder's name: ")
        
        account_number = input("Enter account number: ")
        
        initial_deposit = float(input("Enter initial deposit amount: "))
        
        interest_rate = float(input("Enter annual interest rate (in %): "))

        new_acct = BankAcct(name, account_number, initial_deposit, interest_rate)
        
        print("\nNew Account Created:")
        
        print(new_acct)
    
    else:
        
        print("Invalid choice. Please restart the program and select either 1 or 2.")