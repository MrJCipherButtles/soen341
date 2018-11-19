from models.item import Item
from models.loanable import Loanable


class Book(Item, Loanable):
    def __init__(self, title=None, author=None, num_pages=None, publisher=None, year_published=None, language=None,
                 isbn_10=None, isbn_13=None, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.publisher = publisher
        self.year_published = year_published
        self.language = language
        self.isbn_10 = isbn_10
        self.isbn_13 = isbn_13
        self.object_class = 'Book'
