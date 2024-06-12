
balance = 1000

while True:
    print("1.balance")
    print("2.withdraw")
    print("3.deposit")
    print("4.Exit")
    choice = input("choose an option: ")

    if choice == "1":
        print(f"balance is {balance}")
    elif choice == "2":
        withdraw_balance = int(input("enter withdraw amount: "))
        if withdraw_balance <= balance:
            balance -= withdraw_balance
            print(f"withdraw succesful. , remaining balance is {balance}")
        else:
            print("balance is low")
    elif choice == "3":
        deposit_balance = int(input("enter deposit amount: "))
        balance += deposit_balance
        print(f"deposit is succefull. , remaining balance is {balance}")
    elif choice == "4":
        print("exit")
        break
    else:
        print("wrong choice")