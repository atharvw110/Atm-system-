name = ""
mobile = ""
balance = 0.0

def new_acc():
    global name, mobile, balance
    
    print("\n----- CREATE ACCOUNT -----")
    name = input("Enter account holder name: ")
    mobile = input("Enter mobile number: ")
    balance = float(input("Enter initial balance: "))
    
    print("\nAccount created successfully!")
    print("Account Holder:", name)
    print("Mobile Number:", mobile)
    print("Balance:", balance)

def deposit():
    global balance
    
    if name == "":
        print("\nPlease create an account first.")
        return
        
    print("\n----- DEPOSIT MONEY -----")
    amount = float(input("Enter money to deposit: "))
    
    if amount > 0:
        balance = balance + amount
        print("Money deposited successfully!")
        print("Current Balance:", balance)
    else:
        print("Enter a valid amount.")

def withdraw():
    global balance
    
    if name == "":
        print("\nPlease create an account first.")
        return
        
    print("\n----- WITHDRAW MONEY -----")
    amount = float(input("Enter money to withdraw: "))
    
    
    if amount > 0:
        if amount <= balance:
            balance = balance - amount
            print("Money withdrawn successfully!")
            print("Current Balance:", balance)
        else:
            print("Insufficient balance!")
    else:
        print("Enter a valid amount.")


while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        new_acc()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for using the banking system!")