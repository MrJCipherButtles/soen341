from models.item import Item


class Magazine(Item):
    def __init__(self, title=None, publisher=None, year_published=None, language=None, isbn_10=None, isbn_13=None, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.publisher = publisher
        self.year_published = year_published
        self.language = language
        self.isbn_10 = isbn_10
        self.isbn_13 = isbn_13
        self.object_class = 'Magazine'