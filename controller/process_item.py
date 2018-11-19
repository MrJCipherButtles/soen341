from models.book import Book
from models.magazine import Magazine
from models.movie import Movie
from models.music import Music
from flask import redirect, url_for, render_template


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
        fields = request.form
        item_id = fields['ID']
        item_type = db_connection.get_item_by_id(item_id).object_class

        db_connection.edit_item(item_type, fields, item_id)
        return redirect(url_for('home'))
        

    @staticmethod
    def remove(request, db_connection):
        db_connection.remove_item(request.form['id'])
        return redirect(url_for('home'))
    
    @staticmethod
    def view_item(request, db_connection):
        return redirect(url_for('view_edit_item', itemId=request.form['id'], is_admin=db_connection.verify_admin(request.cookies.get('username'))))
