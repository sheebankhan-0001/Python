#empty dictionary
contacts = {}

while True:
    print('\nContact Book App')
    print('1. Create Conatct')
    print('2. View Contact')
    print('3. Update Conatact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contact')
    print('7. Exit')

    choice = input("Enter your Choice = ")
    if choice == "1":
        name = input("Enter the name = ")
        if name in contacts:
            print(f'Contact name {name} already exists!')
        else:
            age = input("Enter Age = ")
            print("Enter mobile number = ")
            mobile = int(input())
            contacts[name]={"age" :int(age), "mobile" :mobile}
            print(f'Contact name {name} has been created succesfully!')
    elif choice == "2":
        name = input("Enter contact name to view = ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age: {age}, Mobile number :{mobile}")
        else:
            print("Contact not found")
    elif choice == "3":
        name = input("Enter name to update contact = ")
        if name in contacts:
            age = input("Enter Updated  Age = ")
            print("Enter updated mobile number = ")
            mobile = int(input())
            contacts[name] = {"age": int(age), "mobile": mobile}
        else:
            print("Contact not found")
    elif choice == "4":
        name = input("Enter contact name to delete :")
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been deleted sucessfully")
        else:
            print("Contact not found")
    elif choice == "5":
        search_name =input("Enter contact name to search : ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found - Name: {name}, Age: {age}, Mobile Number: {mobile}")
                found = True
        if not found:
            print("No contact found with that name")
    elif choice == "6":
        print(f"Total contacts in your Book : {len(contacts)}")

    elif choice == "7":
        print("Good Bye Contact closed")
        break
    else:
        print("Invalid Input")