class Client:
    def __init__(self, first_name, last_name, address, email, phone):
        self.first = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.phone = phone

    def is_authenticated(self):
        return True  # Can only be called if client exists, can only exist if user is authenticated
