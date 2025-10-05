# test_contact_manager.py

import unittest
import contact_manager


class TestContactManager(unittest.TestCase):
    def test_add_contact(self):
        """Test adding a contact."""
        contact_manager.contacts.clear()
        contact_manager.add_contact("Vanilla", "612-890-1234")
        self.assertIn("Vanilla", contact_manager.contacts)
        self.assertEqual(contact_manager.contacts["Vanilla"], "612-890-1234")

    def test_finding_existing_contact(self):
        """Test finding an existing contact."""
        contact_manager.contacts.clear()
        contact_manager.add_contact("Anna", "612-123-4567")
        phone_number = contact_manager.find_contact("Anna")
        self.assertEqual(phone_number, "612-123-4567")

    def test_finding_nonexistent_contact(self):
        """Test finding a non-existent contact."""
        contact_manager.contacts.clear()
        phone_number = contact_manager.find_contact("Non-existent Contact")
        self.assertIsNone(phone_number)


if __name__ == "__main__":
    unittest.main()