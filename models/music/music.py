from models.item.item import Item


class Music(Item):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
