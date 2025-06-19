import json
from .models import Contact
import uuid

class ContactManager:
    def __init__(self):
        self.contacts = []
        
    def add(self, contact):
        self.contacts.append(contact)
        
    def get(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        
    def remove(self, first_name, last_name):
        for i in range(len(self.contacts - 1)):
            if self.contacts[i].first_name == first_name and self.contacts[i].last_name == last_name:
                removed = self.contacts.pop(i)
                
    def update(self, first_name, last_name, number=None, email=None, tags=[]):
        # if invalid args, return error
        if not first_name and not last_name:
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
        
    def display(self):
        # title
        print(("#" * 31) + "CONTACTS" + ("#" * 31))
        # header
        print("{0: <12} | {1: <12} | {2: <14} | {3: <12}".format("First Name", "Last Name", "Phone Number", "Email"))
        print("-" * 70)
        for contact in self.contacts:
            number_list = [d for d in str(contact.number)]
            
            # construct number with formatting
            number = "(" + number_list[0] + number_list[1] + number_list[2] + ") " + number_list[3] + number_list[4] + number_list[5] + " " + number_list[6] + number_list[7] + number_list[8] + number_list[9]
            print("{0: <12} | {1: <12} | {2: <14} | {3: <12}".format(contact.first_name, contact.last_name, number, contact.email))
        print("#" * 70)
