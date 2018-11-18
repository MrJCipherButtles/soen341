from flask import render_template
from models.book.book import Book
from models.magazine.magazine import Magazine
from models.movie.movie import Movie
from models.music.music import Music


class SearchItem:
    @staticmethod
    def searchItem(db, request):
        name_to_class = {'Book': Book, 'Movie': Movie, 'Magazine': Magazine, 'Music': Music}
        Class = name_to_class[request.form['media_type']]
        html_types = request.form['media_type'].lower()+'s'
        dic = {}

        for key in request.form.keys():
            if request.form[key] != '' and key != "media_type" and key!= 'myList':
                dic[key] = request.form[key]
        items = db.get_all(Class, dictionary=dic)

        html_type = {'books':[], 'magazines':[], 'movies':[], 'musics':[]}
        html_type[html_types]= items
        return render_template('search_results.html', books = html_type['books'], magazines = html_type['magazines'], movies = html_type['movies'], musics = html_type['musics'], is_admin=db.verify_admin(request.cookies.get('username')))


