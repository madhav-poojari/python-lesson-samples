# Bank Account

balance = 0

print("Welcome to your Bank Account!")

while True:
    print("\nMenu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Your balance is:", balance)
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit successful. Your new balance is:", balance)
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful. Your new balance is:", balance)
        else:
            print("Insufficient funds!")
    elif choice == '4':
        print("Thank you for using your Bank Account!")
        break
    else:
        print("Invalid choice!")
