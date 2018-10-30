from models.item.item import Item


class Book(Item):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
