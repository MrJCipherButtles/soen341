from models.book import Book
from models.magazine import Magazine
from models.movie import Movie
from models.music import Music
from flask import redirect, url_for


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
    def edit(request, db_connection):
        ItemId = request.form['id']
        print('id')

    @staticmethod
    def remove(request, db_connection):
        db_connection.remove_item(request.form['id'])
        return redirect(url_for('home'))
