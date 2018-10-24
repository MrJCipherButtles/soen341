from models.item.item_mapper import ItemMapper


class BookMapper(ItemMapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
