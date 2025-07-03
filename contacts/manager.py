import json
from .models import Contact
import json
import os

class ContactManager:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self, first_name, last_name, number=None, email=None, tags=[]):
        new_contact = Contact(first_name, last_name, number, email, tags)
        self.contacts.append(new_contact)
        
    def get_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        return None
            
    def get_contacts(self):
        return self.contacts
        
    def remove(self, first_name, last_name):
        for i in range(len(self.contacts - 1)):
            if self.contacts[i].first_name == first_name and self.contacts[i].last_name == last_name:
                removed = self.contacts.pop(i)
                
    def update(self, first_name, last_name, number=None, email=None, tags=None):
        # if invalid args, return error
        if not first_name or not last_name:
            return "ERROR: First and and last name required."
        
        # find contact
        contact = self.get(first_name, last_name)
        
        if number:
            contact.number = number
            
        if email:
            contact.email = email
            
        if tags:
            contact.tags = tags
            
    
    def sort(self):
        """Sorts the contacts list and returns the sorted list. The original list remains unchanged.

        Returns:
            list: the sorted list
        """
        temp = self.contacts
        self.contacts.sort()
        sorted_contacts = self.contacts
        self.contacts = temp
        return sorted_contacts
    
    def search(self, text):
        # write search algo for partial strings
        return
    
    def filter_by_tag(self, tag):
        output = []
        for contact in self.contacts:
            if tag in contact.tags:
                output.append(contact)
                
    def save_to_file(self, file_name="contacts.out"):
        # convert contacts list to JSON-ready format
        contacts_output = {"contacts": []}
        for contact in self.contacts:
            contacts_output["contacts"].append({"first_name": contact.first_name, "last_name": contact.last_name, "number": contact.number, "email": contact.email, "tags": contact.tags})
        
        with open(file_name, 'w') as f:
            json.dump(contacts_output, f, indent=4)
            
        print("Wrote contact info to", file_name)
        
    def format_number(self, number):
        number_list = [d for d in str(number)]
            
        # construct number with formatting
        return "(" + number_list[0] + number_list[1] + number_list[2] + ") " + number_list[3] + number_list[4] + number_list[5] + "-" + number_list[6] + number_list[7] + number_list[8] + number_list[9]
        
    def display_one(self, first_name, last_name):
        contact = self.get_contact(first_name, last_name)
        if not contact:
            return -1
        print("{0: <12} | {1: <12} | {2: <14} | {3: <12}".format("First Name", "Last Name", "Phone Number", "Email"))
        print("-" * 70)
        for contact in self.contacts:
            if not contact.number:
                number = "Not set"
            else:
                number = self.format_number(contact.number)
                
            email = ""
            if not contact.email:
                email = "Not set"
            else:
                email = contact.email
        print("{0: <12} | {1: <12} | {2: <14} | {3: <12}".format(contact.first_name, contact.last_name, number, email))
        
    def display_all(self):
        # title
        print(("#" * 31) + "CONTACTS" + ("#" * 31))
        # header
        print("{0: <12} | {1: <12} | {2: <14} | {3: <12}".format("First Name", "Last Name", "Phone Number", "Email"))
        print("-" * 70)
        for contact in self.contacts:
            if not contact.number:
                number = "Not set"
            else:
                number = self.format_number(contact.number)
                
            email = ""
            if not contact.email:
                email = "Not set"
            else:
                email = contact.email
            print("{0: <12} | {1: <12} | {2: <14} | {3: <12}".format(contact.first_name, contact.last_name, number, email))
        print("#" * 70)
        
    def save_contacts(self, filename="contacts_savefile.json"):
        # convert contacts to dictionary
        output = []
        for contact in self.contacts:
            contact_dict = {}
            contact_dict["First Name"] = contact.first_name
            contact_dict["Last Name"] = contact.last_name
            contact_dict["Number"] = contact.number
            contact_dict["Email"] = contact.email
            contact_dict["Tags"] = contact.tags
            
            output.append(contact_dict)
            
        # save to file
        with open(filename, "w") as f:
            json.dump(output, f, indent=4)
            print("Contacts saved to", filename)
            
    def save_contacts_ndjson(self, filename="contacts_savefile.ndjson"):
        """Save contacts contained in the contacts list to a file in the NDJSON format.
        This format is required for using the read_data function.

        Args:
            filename (str, optional): The path/filname that contacts will be saved to.
            Defaults to "contacts_savefile.ndjson".
        """
        
        # convert contacts to dictionary
        with open(filename, "w") as f:
            for contact in self.contacts:
                contact_dict = {}
                contact_dict["First Name"] = contact.first_name
                contact_dict["Last Name"] = contact.last_name
                contact_dict["Number"] = contact.number
                contact_dict["Email"] = contact.email
                contact_dict["Tags"] = contact.tags
                
                # writes contacts directly and deliminates with a new line character
                f.write(json.dumps(contact_dict) + "\n")
            
            print("Contacts saved in NDJSON format to", filename)
            
    def load_contacts(self, filename):
        """Reads contacts from a NDJSON formatted file. Uses a generator to improve
        performance for large files.

        Args:
            filename (str): File name of the file that contains contacts

        Yields:
            iterator: a single contact
        """
        with open(filename, "r") as f:
            for line in f:
                yield json.loads(line)
    
    def read_data_no_gen(self, filename):
        """Reads contacts from a JSON file using only an iterator.

        Args:
            filename (str): Filename of the file that contains the contacts
            
        Returns:
            List: The entire list of contacts
        """
        with open(filename, "r") as f:
            return json.load(f)
                
            
    def load_contacts_no_gen(self, filename="contacts_savefile.json"):
        """_summary_

        Args:
            filename (str, optional): _description_. Defaults to "contacts_savefile.json".
        """
        if os.path.exists(filename):
            # load contacts from file
            with open(filename, "r") as f:
                contacts_json = json.load(f)
                for contact in contacts_json:
                    self.add_contact(contact["First Name"], contact["Last Name"], contact["Number"], contact["Email"], contact["Tags"])
                print("Contacts loaded from", filename)