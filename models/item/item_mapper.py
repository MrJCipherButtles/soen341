from abc import ABC


class ItemMapper(ABC):
    def __init__(self, table_data_gateway):
        self.tdg = table_data_gateway
