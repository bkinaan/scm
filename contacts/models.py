import uuid
from functools import total_ordering

# defines contact model
@total_ordering # descriptor to provide remaining comparator functions
class Contact:
    def __init__(self, first_name, last_name, number=None, email=None, tags=None):
        self.id = uuid.uuid4() # creates an internal unique id for each contact
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email
        self.tags = tags or []
        
    def get_id(self):
        return self.id
        
    def __eq__(self, other):
        return self.id == other.id
    
    def __lt__(self, other):
        if self.last_name == other.last_name:
            if self.first_name == other.first_name:
                return self.id < other.id
            return self.first_name < other.first_name
        return self.last_name < other.last_name