def display_friends(contacts):
    print("Friends List: ")
    for name, number in contacts.items():
        print(f"Name : {name}\t\t Number{number}")

def add_friend(contacts, name, number):
    contacts[name] = number
    print("Friend added successfully.")

def delete_friend(contacts, name):
    if name in contacts:
        del contacts[name]
        print("Friend deleted successfully.")
    else:
        print("Friend not found.")

def modify_phone_number(contacts, name, new_number):
    if name in contacts:
        contacts[name] = new_number
        print("Phone number modified successfully.")
    else:
        print("Friend not found.")

def check_friend_presence(contacts, name):
    if name in contacts:
        print(f"{name} is present in the dictionary.")
    else:
        print(f"{name} is not present in the dictionary.")

def display_sorted_contacts(contacts):
    sorted_contacts = sorted(contacts.items())
    print("Sorted Contacts:")
    for name, number in sorted_contacts:
        print(f"{name}\t\t{number}")

def main():
    contacts = {}

    while True:
        print("\n1. Display all friends")
        print("2. Add a new friend")
        print("3. Delete a friend")
        print("4. Modify phone number")
        print("5. Check friend presence")
        print("6. Display sorted contacts")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_friends(contacts)
        elif choice == '2':
            name = input("Enter friend's name: ")
            number = input("Enter friend's phone number: ")
            add_friend(contacts, name, number)
        elif choice == '3':
            name = input("Enter friend's name to delete: ")
            delete_friend(contacts, name)
        elif choice == '4':
            name = input("Enter friend's name to modify phone number: ")
            new_number = input("Enter new phone number: ")
            modify_phone_number(contacts, name, new_number)
        elif choice == '5':
            name = input("Enter friend's name to check presence: ")
            check_friend_presence(contacts, name)
        elif choice == '6':
            display_sorted_contacts(contacts)
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
