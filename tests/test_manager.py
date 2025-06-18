import unittest
from contacts.models import Contact

class TestContact(unittest.TestCase):
    def test_contact_initialization(self):
        os.chdir(BASE_PATH + "/")
        contact = Contact("Alice", "Smith", "4642336443", "alice@website.com")
        self.assertEqual(contact.first_name, "Alice")
        self.assertEquals(contact.last_name, "Smith")
        self.assertEquals(contact.number, "4642336443")
        self.assertEquals(contact.email, "alice@website.com")
        
if __name__ == "__main__":
    unittest.main()