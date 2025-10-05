"""
test_contact_manager.py

Unit tests for contact_manager.py.

Test Cases:
- Adding a new contact (ensures add_contact correctly adds a contact to the dictionary).
- Finding an existing contact (ensures find_contact correctly returns a contact's phone number).
- Finding a non-existent contact (ensures find_contact gracefully handles a non-existent contact).
- Deleting an existing contact (ensures delete_contact successfully removes a contact).
- Deleting a non-existent contact (ensures delete_contact handles a non-existent contact without crashing).
- Adding a duplicate contact (checks if add_contact raises the DuplicateContactError using self.assertRaises()).

Usage:
    Run all tests with:
        python -m unittest test_contact_manager.py
"""

import unittest
from contact_manager import ContactManager, DuplicateContactError

cm = ContactManager()


class TestContactManager(unittest.TestCase):
    """
    Unit tests for the contact_manager module.

    This TestContactManager class tests the core functions of the contact manager, including:
    - Adding new contacts
    - Finding existing and non-existing contacts
    - Deleting existing and non-existing contacts
    - Handling duplicate contacts

    Uses unittest framework to verify that all functions work correctly and handle
    errors gracefully.
    """

    def test_add_contact(self):
        """
        Test adding a contact.

        Ensure add_contact correctly adds a contact to the dictionary
        and stores the correct phone number.
        """
        cm = ContactManager()
        cm.add_contact("Vanilla", "612-890-1234")
        self.assertIn("Vanilla", cm.contacts)
        self.assertEqual(cm.contacts["Vanilla"], "612-890-1234")

    def test_finding_existing_contact(self):
        """
        Test finding an existing contact.

        Ensures that find_contact returns the correct phone number
        for a contact that exists in the contacts dictionary.
        """
        cm = ContactManager()
        cm.add_contact("Anna", "612-123-4567")
        phone = cm.find_contact("Anna")
        self.assertEqual(phone, "612-123-4567")

    def test_finding_nonexistent_contact(self):
        """
        Test finding a non-existent contact.

        Ensure that find_contact gracefully handles searches
        for contacts that do not exist, returning None and
        not raising an exception.
        """
        cm = ContactManager()
        phone = cm.find_contact("Non-existent Contact")
        self.assertIsNone(phone)
    
    def test_delete_existing_contact(self):
        """
        Test deleting an existing contact.

        Ensures that delete_contact successfully removes a contact from dictionary.
        """
        contact_manager.contacts.clear()
        contact_manager.add_contact("Existing Contact", "612-123-4567")
        contact_manager.delete_contact("Existing Contact")
        self.assertNotIn("Existing Contact", contact_manager.contacts)
        self.assertEqual(contact_manager.contacts, {})

    def test_delete_nonexistent_contact(self):
        """
        Test deleting a non-existing contact.

        Ensures that delete_contact handles deletion attempts
        for contacts that do not exist without crashing or
        raising an exception.
        """
        contact_manager.contacts.clear()
        contact_manager.delete_contact("Non-existent Contact")
        self.assertEqual(contact_manager.contacts, {})

    def test_adding_duplicate_contact(self):
        """
        Test adding a duplicate contact.

        Ensures that attempting to add a contact that already
        exists raises a DuplicateContactError.
        """
        contact_manager.contacts.clear()
        contact_manager.add_contact("Anna", "612-123-4567")
        self.assertRaises(
            contact_manager.DuplicateContactError,
            contact_manager.add_contact,
            "Anna", "612-123-4567"
        )


if __name__ == "__main__":
    unittest.main()
