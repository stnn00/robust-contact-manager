"""
contact_manager.py

Refactored version of starter script buggy_contacts.py
providing a command-line contact manager with
improved error handling, input validation, and
a custom exception for catching duplicate contacts.

Features:
1. Add new contacts, preventing duplicates with DuplicateContactError.
2. Search for contacts by name, with user-friendly messages for non-existent entries.
3. Delete contacts, safely handling attempts to remove non-existent contacts.
4. Optional manual testing of core functions with the RUN_TESTS flag.

main() function launches a command-line menu for user interactions to perform contact operations.
"""

contacts = {}


class DuplicateContactError(Exception):
    """Custom exception class to raise an exception when attempting to add a contact that already exists."""
    pass


def add_contact(name, phone):
    """
    Add a new contact to the contacts dictionary.

    Args:
        name (str): The contact's name.
        phone (str): The contact's phone number.

    Raises:
        DuplicateContactError: If the contact already exists.
    
    Returns:
        None
    """
    if name in contacts:
        raise DuplicateContactError(f"[add_contact] {name} already exists.")
    contacts[name] = phone
    print(f"[add_contact] Added {name} ({phone}) to contacts.")


def find_contact(name):
    """
    Finds a contact's phone number, prints a message if the contact exists or not.

    Args:
        name (str): The contact's name.
    
    Returns:
        str or None: The phone number if found, otherwise None.
    """
    try:
        print(f"[find_contact] Found '{name}': {contacts[name]}")
        return contacts[name]
    except KeyError:
        print(f"[find_contact] Contact '{name}' not found.")
        return None


def delete_contact(name):
    """
    Deletes a contact from the contacts dictionary.

    Prints a message indicating whether deletion was successful or if the contact doesn't exist.

    Args:
        name (str): The contact's name.
    """
    try:
        del contacts[name]
        print(f"[delete_contact] Successfully deleted {name}.")
    except KeyError:
        print(f"[delete_contact] Contact '{name}' not found.")


def main():
    """
    Runs the command-line menu for the contact manager.

    Handles invalid input and prints readable messages.
    """
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
        if choice == 1:
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            try:
                add_contact(name, phone)
            except DuplicateContactError as e:
                print(f"An error occurred: {e}")
        elif choice == 2:
            name = input("Enter name to find: ")
            find_contact(name)
        elif choice == 3:
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == 4:
            break
        else:
            print("Invalid choice.")


RUN_TESTS = False

if RUN_TESTS:
    test_contacts = {"Anna": "612-123-4567"}
    contacts.update(test_contacts)

    find_contact("Anna")
    find_contact("Maya")

    try:
        add_contact("Anna", "612-123-4567")
    except DuplicateContactError as e:
        print(e)
    
    delete_contact("Anna")


if __name__ == "__main__":
    main()
