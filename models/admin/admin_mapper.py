from models.client.client_mapper import ClientMapper


class AdminMapper(ClientMapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
