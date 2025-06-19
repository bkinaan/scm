import unittest
from contacts.models import Contact
from contacts.manager import ContactManager

class TestContact(unittest.TestCase):
    def test_contact_initialization(self):
        contact = Contact("Alice", "Smith", "4642336443", "alice@website.com")
        self.assertEqual(contact.first_name, "Alice")
        self.assertEqual(contact.last_name, "Smith")
        self.assertEqual(contact.number, "4642336443")
        self.assertEqual(contact.email, "alice@website.com")
        
    def test_contact_equality(self):
        c1 = Contact("Bob", "Smith")
        c2 = Contact("Bob", "Smith")
        c1.id = c2.id # only for testing
        self.assertEqual(c1, c2)
        
    def test_contact_less_than(self):
        c1 = Contact("Bob", "Smith", 4633464644, "bob@bob.com")
        c2 = Contact("Alice", "Tufts", 3532335443, "yuh@alice.com")
        c3 = Contact("Alice", "Tufts", 3452335323, "other_alice@tufts.com")
        c2.id = 0 # only for testing
        c3.id = 1 # only for testing
        
        self.assertEqual(c1 < c2, True)
        self.assertEqual(c1 > c2, False)
        self.assertEqual(c3 > c2, True)
        
    def test_sorting_contact_manager(self):
        c1 = Contact("Bob", "Smith", 4633464644, "bob@bob.com")
        c2 = Contact("Alice", "Tufts", 3532335443, "yuh@alice.com")
        c3 = Contact("Alice", "Creaton", 3452335323, "other_alice@tufts.com")
        
        manager = ContactManager()
        manager.add(c1)
        manager.add(c2)
        manager.add(c3)
        
        sorted_contacts = manager.sort()
        self.assertEqual(sorted_contacts[0].last_name, "Creaton")
        
if __name__ == "__main__":
    unittest.main()