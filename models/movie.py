from models.item import Item
from models.loanable import Loanable


class Movie(Item, Loanable):
    def __init__(self, title=None, director=None, producer=None, actors=None, languages=None, subtitles=None,
                 dubbed=None, release_date=None, runtime=None, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.director = director
        self.producer = producer
        self.actors = actors
        self.languages = languages
        self.subtitles = subtitles
        self.dubbed = dubbed
        self.release_date = release_date
        self.runtime = runtime
        self.object_class = 'Movie'
