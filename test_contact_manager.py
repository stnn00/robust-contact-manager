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


if __name__ == "__main__":
    unittest.main()