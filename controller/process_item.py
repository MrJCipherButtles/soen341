from controller.controller import Controller
from models.book import Book
from models.magazine import Magazine
from models.movie import Movie
from models.music import Music
from flask import redirect, url_for, render_template, request


class ProcessItem(Controller):
    def add(self):
        name_to_class = {'BOOK': Book, 'MOVIE': Movie, 'MAGAZINE': Magazine, 'MUSIC': Music}
        Class = name_to_class[request.form['media_type']]
        kwargs = {}
        for key, item in request.form.items():
            if key == "object_class":
                continue
            kwargs[key] = item
        item = Class(**kwargs)
        self.db.insert_item(item)

    def edit(self):
        fields = request.form
        item_id = fields['ID']
        item_type = self.db.get_item_by_id(item_id).object_class

        self.db.edit_item(item_type, fields, item_id)
        return redirect(url_for('home'))
        

    def remove(self):
        self.db.remove_item(request.form['id'])
        return redirect(url_for('home'))
    
    def view_item(self):
        return redirect(url_for('view_edit_item', itemId=request.form['id'], is_admin=self.db.verify_admin(request.cookies.get('username'))))
