
contacts = []

while True:
    print("1.add contact")
    print("2.view contacts")
    print("3.delete contacts")
    print("4.exit")
    choice = input("choose an option: ")

    if choice == "1":
        contact = input("enter a new contact: ")
        contacts.append(contact)
        print("contact added.\n")
    elif choice == "2":
        if contacts:
            for i,contact in enumerate(contacts, start=1):
                print(f"{i}. {contact}")
        else:
            print("no contacts.\n")

    elif choice == '3':
        if contacts:
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. {contact}")
            try:
                num = int(input("enter contact number to remove: "))
                contacts.pop(num - 1)
                print("contact removed.\n")

            except (ValueError, IndexError):
                print("invalid number.\n")
        else:
            print("no contacts to remove\n")
    elif choice == '4':
        print("bye")
        break
    else:
        print("invalid choice, try again,\n")
#created by atharv joshi
#contact book