import uuid

# defines contact model
class Contact:
    def __init__(self, first_name, last_name, number, email, tags=None):
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
    
    def __lt__(self, other, by='last_name'):
        if by == 'first_name':
            return self.first_name < other.first_name
        elif by == 'last_name':
            return self.last_name < other.last_name
        elif by == 'email':
            return self.email < other.email
        elif by == 'number':
            return self.number < other.number
        
    def __gt__(self, other, by='last_name'):
        if by == 'first_name':
            return self.first_name > other.first_name
        elif by == 'last_name':
            return self.last_name > other.last_name
        elif by == 'email':
            return self.email > other.email
        elif by == 'number':
            return self.number > other.number