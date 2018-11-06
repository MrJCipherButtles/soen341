from models.item.item import Item


class Music(Item):
    def __init__(self, type=None, title=None, release_date=None, artist=None, label=None, asin=None, **kwargs):
        super().__init__(**kwargs)
        self.type = type
        self.title = title
        self.release_date = release_date
        self.artist = artist
        self.label = label
        self.asin = asin
