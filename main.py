from contacts import Contact, ContactManager, validators as v
import sys

def main():
    manager = ContactManager()
    
    while True:
        print("""
              ------------------
              CONTACT MANAGER
              -------------------
              Options:
              -------------------
              1) View contacts
              2) Add contact
              3) Edit contact
              4) Remove contact
              5) Exit
              -------------------
              """)
        choice = input("Choose an option: ")
        
        if choice == "1":
            # display all contacts
            if manager.get_contacts() == []:
                print("You don't have any contacts. Add some to see them here.")
                continue
            manager.display_all()
        elif choice == "2":
            # add contact
            first_name = input("Please enter their first name (required): ")
            last_name = input("Please enter their last name (required): ")
            number = input("Please enter their number (optional, press enter to skip): ")
            email = input("Please enter their email (optional, press enter to skip): ")
            
            if first_name == "":
                print("ERROR: First name required. Contact not created.")
                continue
            else:
                if not v.validate_name(first_name):
                    print("ERROR: First name can only contain alpahbet characters and spaces. Contact not created.")
                    continue
                    
            if last_name == "":
                print("ERROR: Last name required. Contact not created.")
                continue
            else:
                if not v.validate_name(last_name):
                    print("ERROR: Last name can only contain alpahbet characters and spaces. Contact not created.")
                    continue
                
            
            if number == "":
                number = None
            else:
                if not v.validate_number(number):
                    print("ERROR: Number must contain only 10 digits. Contact not created.")
                    continue
            
            if email == "":
                email = None
            else:
                if not v.validate_email(email):
                    print("ERROR: Email must be in the format of user@site.com. Contact not created.")
                    continue
            
            manager.add_contact(first_name, last_name, number, email)
            print("Contact created successfully")
        elif choice == "3":
            # edit contact
            first_name = input("Enter the first name of the contact you want to edit: ")
            last_name = input("Enter the last name of the contact you want to edit: ")
            
            contact = manager.get_contact(first_name, last_name)
            
            if not contact:
                print("Contact not found.")
                continue
            else:
                manager.display_one(contact.first_name, contact.last_name)
                print("""
                      What do you want to update?
                      1) First name
                      2) Last name
                      3) Number
                      4) Email
                      5) Cancel
                      """)
                choice = input("Select an option: ")
                
                if choice == "1":
                    new_first_name = input("Enter the new first name: ")
                    if not v.validate_name(new_first_name):
                        print("ERROR: First name can only contain alpahbet characters and spaces. Contact not updated.")
                        continue
                    contacts = manager.get_contacts()
                    idx = contacts.index(contact)
                    edit_contact = contacts.pop(idx)
                    edit_contact.first_name = new_first_name
                    contacts.append(edit_contact)
                elif choice == "2":
                    new_last_name = input("Enter the new last name: ")
                    if not v.validate_name(new_last_name):
                        print("ERROR: Last name can only contain alpahbet characters and spaces. Contact not updated.")
                        continue
                    contacts = manager.get_contacts()
                    idx = contacts.index(contact)
                    edit_contact = contacts.pop(idx)
                    edit_contact.last_name = new_last_name
                    contacts.append(edit_contact)
                elif choice == "3":
                    new_number = input("Enter the new number: ")
                    if not v.validate_number(new_number):
                        print("ERROR: Number must contain 10 digits. Contact not updated.")
                        continue
                    contacts = manager.get_contacts()
                    idx = contacts.index(contact)
                    edit_contact = contacts.pop(idx)
                    edit_contact.number = new_number
                    contacts.append(edit_contact)
                elif choice == "4":
                    new_email = input("Enter the new email: ")
                    if not v.validate_email(new_email):
                        print("ERROR: Email must be in the format of user@site.com. Contact not updated.")
                        continue
                    contacts = manager.get_contacts()
                    idx = contacts.index(contact)
                    edit_contact = contacts.pop(idx)
                    edit_contact.email = new_email
                    contacts.append(edit_contact)
                else:
                    continue
        elif choice == "4":
            # remove contact
            first_name = input("Enter the first name of the contact you want to remove: ")
            last_name = input("Enter the last name of the contact you want to remove: ")
            
            contact = manager.get_contact(first_name, last_name)
            
            if not contact:
                print("Contact not found.")
                continue
            else:
                contacts = manager.get_contacts()
                idx = contacts.index(contact)
                edit_contact = contacts.pop(idx)    
        else:
            sys.exit()
            
if __name__ == "__main__":
    main()