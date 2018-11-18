from models.client import Client


class Admin(Client):
    # Has methods that client does not
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
