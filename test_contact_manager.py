# test_contact_manager.py

import unittest
import contact_manager


class TestContactManager(unittest.TestCase):

    def test_add_contact(self):
        """
        Test adding a contact.
        Ensure add_contact correctly adds a contact to the dictionary.
        """
        contact_manager.contacts.clear()
        contact_manager.add_contact("Vanilla", "612-890-1234")
        self.assertIn("Vanilla", contact_manager.contacts)
        self.assertEqual(contact_manager.contacts["Vanilla"], "612-890-1234")

    def test_finding_existing_contact(self):
        """
        Test finding an existing contact.
        Ensure find_contact correctly returns a contact's phone number
        """
        contact_manager.contacts.clear()
        contact_manager.add_contact("Anna", "612-123-4567")
        phone_number = contact_manager.find_contact("Anna")
        self.assertEqual(phone_number, "612-123-4567")

    def test_finding_nonexistent_contact(self):
        """
        Test finding a non-existent contact.
        Ensure find_contact gracefully handles a non-existent contact.
        """
        contact_manager.contacts.clear()
        phone_number = contact_manager.find_contact("Non-existent Contact")
        self.assertIsNone(phone_number)
    
    def test_delete_existing_contact(self):
        """
        Test deleting an existing contact.
        Ensure delete_contact successfully removes a contact.
        """
        contact_manager.contacts.clear()
        contact_manager.add_contact("Existing Contact", "612-123-4567")
        contact_manager.delete_contact("Existing Contact")
        self.assertNotIn("Existing Contact", contact_manager.contacts)
        self.assertEqual(contact_manager.contacts, {})

    def test_delete_nonexistent_contact(self):
        """
        Test deleting a non-existing contact.
        Ensure delete_contact handles a non-existent contact without crashing.
        """
        contact_manager.contacts.clear()
        contact_manager.delete_contact("Non-existent Contact")
        self.assertEqual(contact_manager.contacts, {})

    def test_adding_duplicate_contact(self):
        """
        Test adding a duplicate contact.
        Ensure that attempting to add an existing contact raises DuplicateContactError.
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