from models.item.item import Item


class Magazine(Item):
    def __init__(self, **kwargs, title, publisher, year_published, language, isbn_10, isbn_13):
        super().__init__(**kwargs)
        self.title = title
        self.publisher = publisher
        self.year_published = year_published
        self.language = language
        self.isbn_10 = isbn_10
        self.isbn_13 = isbn_131w