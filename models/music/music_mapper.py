from models.item.item_mapper import ItemMapper


class MusicMapper(ItemMapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
