from flask import render_template, request

from controller.controller import Controller
from models.book import Book
from models.magazine import Magazine
from models.movie import Movie
from models.music import Music


class SearchItem(Controller):
    def searchItem(self):
        name_to_class = {'Book': Book, 'Movie': Movie, 'Magazine': Magazine, 'Music': Music}
        Class = name_to_class[request.form['media_type']]
        html_types = request.form['media_type'].lower()+'s'
        dic = {}

        for key in request.form.keys():
            if request.form[key] != '' and key != "media_type" and key!= 'myList':
                dic[key] = request.form[key]
        items = self.db.get_all(Class, dictionary=dic)

        html_type = {'books':[], 'magazines':[], 'movies':[], 'musics':[]}
        html_type[html_types]= items
        return render_template('search_results.html', books = html_type['books'], magazines = html_type['magazines'], movies = html_type['movies'], musics = html_type['musics'], is_admin=self.db.verify_admin(request.cookies.get('username')), items = items)


