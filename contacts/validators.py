from contacts import Contact, ContactManager
import re

def validate_name(name):
    name_pattern = re.compile("^[A-Za-z ]+$")
    if not re.fullmatch(name_pattern, name):
        return False
    return True


def validate_number(number):
    number_pattern = re.compile("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]")
    if not re.fullmatch(number_pattern, number):
        return False
    return True
    
def validate_email(email):
    email_pattern = re.compile(".*@.*\\..*")
    if not re.fullmatch(email_pattern, email):
        return False
    return True
