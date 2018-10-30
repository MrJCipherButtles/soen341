from models.item.item import Item


class Movie(Item):
    def __init__(self, title, director, producer, actors, languages, subtitles, dubbed, release_date, runtime, **kwargs):
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
