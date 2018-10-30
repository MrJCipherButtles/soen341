from models.item.item import Item


class Music(Item):
    def __init__(self, musictype, title, release_date, artist, label, asin, **kwargs):
        super().__init__(**kwargs)
        self.musictype = musictype
        self.title = title
        self.release_date = release_date
        self.artist = artist
        self.label = label
        self.asin = asin
