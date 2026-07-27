#Smart ATM System

print("Welcome to Varun ATM\n")

balance = 10000  #initial balance

while True:
    print("\nChoose an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Check Balance
    if choice == "1":
        print(f"Your current balance is: ₹{balance}")

#Deposit Money
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        
        if amount > 0:
            balance += amount
            print(f"{amount} deposited successfully!")
        else:
            print("Invalid amount!")

#Withdraw Money
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        
        # Nested if
        if amount > 0:
            if amount <= balance:
                balance -= amount
                print(f"₹{amount} withdrawn successfully!")
            else:
                print("Insufficient balance!")
        else:
            print("Enter a valid amount!")

    # Exit
    elif choice == "4":
        print("Thank you for using My Varun ATM. ")
        break

    else:
        print("⚠️ Invalid choice! Please select 1-4.")    
