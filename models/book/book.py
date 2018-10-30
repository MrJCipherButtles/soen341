from models.item.item import Item


class Book(Item):
    def __init__(self, **kwargs, title, author, num_pages, publisher, year_published, language, isbn_10, isbn_13):
        super().__init__(**kwargs)
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.publisher = publisher
        self.year_published = year_published
        self.language = language
        self.isbn_10 = isbn_10
        self.isbn_13 = isbn_13

