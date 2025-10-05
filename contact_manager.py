# contact_manager.py

contacts = {"Anna": "612-123-4567"}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Added {name} to contacts.")

def find_contact(name):
    try:
        print(contacts[name])
    except KeyError:
        print("Contact not found.")

def delete_contact(name):
    try:
        del contacts[name]
        print(f"Deleted {name}.")
    except KeyError:
        print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid choice. Please enter a number (1-4).")
            continue
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            name = input("Enter name to find: ")
            find_contact(name)
        elif choice == '3':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

RUN_TESTS = True

if RUN_TESTS:
    test_contacts = {"Anna": "612-123-4567"}

    contacts.update(test_contacts)

    find_contact("Anna")
    find_contact("Maya")

    delete_contact("Anna")


if __name__ == "__main__":
    main()
