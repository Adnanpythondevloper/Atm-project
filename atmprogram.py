Balance=1000
pin=1234
print("Welcome to the ATM")
user_pin=int(input("Please enter your pin: "))
if user_pin==pin:
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    choice=int(input("Please select an option: "))
    if choice==1:
        print("Your balance is: ", Balance)
    elif choice==2:
        amount=int(input("Enter the amount to withdraw: "))
        if amount>Balance:
            print("Insufficient funds")
        else:
            Balance-=amount
            print("You have withdrawn: ", amount)
            print("Your new balance is: ", Balance)
    elif choice==3:
        amount=int(input("Enter the amount to deposit: "))
        Balance+=amount
        print("You have deposited: ", amount)
        print("Your new balance is: ", Balance)
    elif choice==4:
        print("Thank you for using the ATM. Goodbye!")
    else:
        print("Invalid option selected")