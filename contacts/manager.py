import json
from .models import Contact
import uuid

class ContactManager:
    def __init__(self):
        self.contacts = []
        
    def add(self, first_name, last_name, number, email, tags):
        contact = Contact(first_name, last_name, number, email, tags)
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
            
    
    def sort(self, by):
        # TODO: write sorting algo
        return
    
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
