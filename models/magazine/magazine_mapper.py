from models.item.item_mapper import ItemMapper


class MagazineMapper(ItemMapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
