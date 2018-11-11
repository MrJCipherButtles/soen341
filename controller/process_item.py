from models.book.book import Book
from models.magazine.magazine import Magazine
from models.movie.movie import Movie
from models.music.music import Music


class ProcessItem():
    @staticmethod
    def add(request, db_connection):
        name_to_class = {'BOOK': Book, 'MOVIE': Movie, 'MAGAZINE': Magazine, 'MUSIC': Music}
        Class = name_to_class[request.form['media_type']]
        kwargs = {}
        for key, item in request.form.items():
            kwargs[key] = item
        item = Class(**kwargs)
        db_connection.insert_item(item)

    @staticmethod
    def remove(request, db_connection):
        db_connection.remove_item(request.form['id'])
        return 'success'
