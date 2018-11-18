from models import Item
from models import Loanable


class Music(Item, Loanable):
    def __init__(self, mediaType=None, title=None, release_date=None, artist=None, label=None, asin=None, **kwargs):
        super().__init__(**kwargs)
        self.mediaType = mediaType
        self.title = title
        self.release_date = release_date
        self.artist = artist
        self.label = label
        self.asin = asin
        self.object_class = 'Music'
