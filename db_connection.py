import hashlib

import datetime
from flaskext.mysql import MySQL
from helper.db_config import db_user, db_password, db_name, db_host
from models.book import Book
from models.magazine import Magazine
from models.movie import Movie
from models.music import Music

class DBGateway:
    def __init__(self, app):
        self.mysql = MySQL()

        # MySQL configurations
        app.config['MYSQL_DATABASE_USER'] = db_user
        app.config['MYSQL_DATABASE_PASSWORD'] = db_password
        app.config['MYSQL_DATABASE_DB'] = db_name
        app.config['MYSQL_DATABASE_HOST'] = db_host
        self.mysql.init_app(app)

        self.conn = self.mysql.connect()
        self.cursor = self.conn.cursor()

        self.class_to_table = {"BOOK": "prints", "MAGAZINE": "prints", "MOVIE": "medias", "MUSIC": "medias"}

    def get_all(self, Class, email=None, dictionary=None):
        res = []
        if dictionary:
            fields = ''
            for key, value in dictionary.items():
                if value.isdigit():
                    fields = fields + " AND " + key + '=' + value
                else:
                    fields = fields + " AND " + key + '=' + "\'" + value + "\'"
            if Class.__name__.upper() == "BOOK" or Class.__name__.upper() == "MAGAZINE":
                type = 'prints'
            else:
                type = 'medias'

            query = "SELECT * FROM %s INNER JOIN items ON itemId = id WHERE items.itemType = '%s' %s;" % (
                type, Class.__name__.upper(), fields)

        elif email:
            query = "SELECT * FROM library.items INNER JOIN loans ON items.id = loans.itemId WHERE items.itemType = '%s' AND loans.clientId = '%s';" % (
                Class.__name__.upper(), email)
        else:
            query = "SELECT * FROM library.items WHERE items.itemType = '%s';" % Class.__name__.upper()

        print("QUERY:   " + query)
        self.cursor.execute(query)
        ids = [res[0] for res in self.cursor.fetchall()]
        if len(ids) == 0:
            return []
        ids_str = self.arr_to_mysqlarr(ids)
        query = "SELECT * FROM library.%s WHERE itemId IN %s;" % (self.class_to_table[Class.__name__.upper()], ids_str)
        print(query)
        self.cursor.execute(
            query
        )
        # print(self.cursor.fetchall())
        data = self.cursor.fetchall()
        args = [d[0] for d in self.cursor.description]
        for record in data:
            kwargs = {}
            for i in range(len(args)):
                kwargs[args[i]] = record[i]
            item = Class(**kwargs)
            res.append(item)
        return res

    def arr_to_mysqlarr(self, arr):
        return "(" + str(arr)[1:len(str(arr)) - 1] + ")"

    def insert_item(self, item):
        """INSERT INTO prints (itemId,title,publisher,year_published,language,isbn_10,isbn_13) -- Magazines
        VALUES
        (16,'Design News','UBM','1946','English','9000119407','987-9000119407');
        """
        vals = [val for key, val in item.__dict__.items()]
        vals = vals[:-1]
        item_query = "INSERT INTO items (loanable, itemType) VALUES ('%s', '%s')" % (
            'N' if type(item).__name__.upper() == 'MAGAZINE' else 'Y', type(item).__name__.upper())
        print(item_query)
        self.cursor.execute(item_query)
        vals[0] = self.cursor.lastrowid
        for i in range(len(vals)):
            if i == 0:
                continue
            if vals[i].isdigit() and len(vals[i]) < 10:
                vals[i] = int(vals[i])

        fields = [key for key, val in item.__dict__.items()]
        fields.remove("object_class")
        fields[0] = "itemId"
        fields = self.arr_to_mysqlarr(fields).replace("'", "")
        vals = self.arr_to_mysqlarr(vals)
        query = "INSERT INTO %s %s VALUES %s;" % (self.class_to_table[type(item).__name__.upper()], fields, vals)
        print(query)
        self.cursor.execute(query)
        self.conn.commit()

    def remove_item(self, id):
        self.cursor.execute("DELETE FROM items WHERE id = %s" % id)
        self.conn.commit()

    def process_return(self, id):
        self.cursor.execute("DELETE FROM loans WHERE itemId = %s" % id)
        self.conn.commit()

    def verify_login(self, user, password):
        h = hashlib.md5(bytes(password, "utf-8"))
        pwd = h.hexdigest()
        self.cursor.execute(
            "SELECT * FROM library.users WHERE email = '%s' AND pswd = '%s'" % (user, pwd))
        self.cursor.fetchall()
        return self.cursor.rowcount != 0

    def verify_admin(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email = '%s' AND privilegeLevel = 'ADMIN'" % email)
        self.cursor.fetchall()
        return self.cursor.rowcount != 0

    def register_user(self, request):
        fname = request.form['firstname']
        lname = request.form['lastname']
        address_1 = request.form['address-1']
        address_2 = request.form['address-2']
        city = request.form['city']
        state = request.form['state']
        postal = request.form['postal']
        country = request.form['country']
        email = request.form['email']
        password = request.form['psw']
        psw_repeat = request.form['psw-repeat']
        phone = request.form['phone']

        if password != psw_repeat:
            return "Passwords do not match"
        h = hashlib.md5(bytes(password, "utf-8"))
        pwd = h.hexdigest()
        self.cursor.execute(
            "INSERT INTO library.users (firstName, lastName, address, email, phone, pswd) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (
                fname, lname, address_1 + ' ' + address_2 + ' ' + city + ' ' + state + ' ' + postal + ' ' + country,
                email, str(phone), pwd))
        self.conn.commit()
        return "registration successful"

    def register_user_admin(self, request):
        fname = request.form['firstname']
        lname = request.form['lastname']
        address_1 = request.form['address-1']
        address_2 = request.form['address-2']
        city = request.form['city']
        state = request.form['state']
        postal = request.form['postal']
        country = request.form['country']
        email = request.form['email']
        password = request.form['psw']
        psw_repeat = request.form['psw-repeat']
        phone = request.form['phone']
        typeuser = 'ADMIN'
        if password != psw_repeat:
            return "Passwords do not match"
        h = hashlib.md5(bytes(password, "utf-8"))
        pwd = h.hexdigest()
        self.cursor.execute(
            "INSERT INTO library.users (firstName, lastName, address, email, phone, pswd, privilegeLevel) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                fname, lname, address_1 + ' ' + address_2 + ' ' + city + ' ' + state + ' ' + postal + ' ' + country,
                email, str(phone), pwd, typeuser))
        self.conn.commit()
        return "registration successful"

    def get_loans_for_user(self, c, email):
        return self.get_all(c, email)
    
    def get_item_by_id(self, id):
        query = "SELECT itemType FROM library.items WHERE id=%s" % (id) #get itemType

        self.cursor.execute(query)
        itemType = self.cursor.fetchone()
        
        if 'BOOK' in itemType:
            query = "SELECT * FROM library.prints WHERE itemId=%s" % (id)
            self.cursor.execute(query)
            t = self.cursor.fetchone()

            item = Book(t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8])
            print()

            return item
            
        elif 'MAGAZINE' in itemType:
            query = "SELECT * FROM library.prints WHERE itemId=%s" % (id)
            self.cursor.execute(query)
            t = self.cursor.fetchone()

            item = Magazine(t[1], t[4], t[5], t[6], t[7], t[8])
            return item
            

            
        elif 'MUSIC' in itemType:
            query = "SELECT * FROM library.medias WHERE itemId=%s" % (id)
            self.cursor.execute(query)
            t = self.cursor.fetchone()

            item = Music(t[1], t[2], t[3], t[4], t[5], t[6])
            return item
            
        elif 'MOVIE' in itemType:
            query = "SELECT * FROM library.medias WHERE itemId=%s" % (id)
            self.cursor.execute(query)
            t = self.cursor.fetchone()

            item = Movie(t[2], t[3], t[7], t[8], t[9], t[10], t[11], t[12], t[13])
            return item

        else:
            print('Error retrieving itemType.')
            return False

        return item
            

        

    def loan_item(self, user, itemID):
        self.cursor.execute("SELECT loanable FROM items WHERE id= %s AND loanable='Y'" % itemID)
        self.cursor.fetchall()
        if self.cursor.rowcount == 0:
            return False
        try:
            self.cursor.execute(
                "INSERT INTO library.loans (clientId, itemId, loan_date) VALUES ('%s', '%s', '%s')" % (
                    user, itemID, datetime.datetime.today().strftime('%Y-%m-%d')))
            self.conn.commit()
        except:
            return False
        return True
        
    def edit_item(self, item_type, fields, item_id):
        if item_type == 'Book':
            query = "UPDATE library.prints SET title='%s', author='%s', num_pages='%s', publisher='%s', year_published=%s, language='%s', isbn_10=%s, isbn_13='%s' WHERE itemId=%s;" % (fields['Title'], fields['Author'], fields['Pages'], fields['Publisher'], fields['Year'], fields['Language'], fields['ISBN_10'], fields['ISBN_13'], item_id)
            print(query)
            self.cursor.execute(query)
            self.conn.commit()
            return True
        if item_type == 'Magazine':
            query = "UPDATE library.prints SET title='%s', publisher='%s', year_published=%s, language='%s', isbn_10=%s, isbn_13='%s' WHERE itemId=%s;" % (fields['Title'], fields['Publisher'], fields['Year'], fields['Language'], fields['ISBN_10'], fields['ISBN_13'], item_id) 
            self.cursor.execute(query)
            self.conn.commit()
            return True
        if item_type == 'Movie':
            query = "UPDATE library.medias SET title='%s', release_date='%s', director='%s', producer='%s', actors='%s', languages='%s', subtitles='%s', dubbed='%s', runtime=%s WHERE itemId=%s;" % (fields['Title'], fields['ReleaseDate'], fields['Director'], fields['Producers'], fields['Actors'], fields['Languages'], fields['Subtitles'], fields['Dubbed'], fields['Run Time'], item_id)
            self.cursor.execute(query)
            self.conn.commit()
            return True
        if item_type == 'Music':
            query = "UPDATE library.medias SET mediaType='%s', title='%s', release_date='%s', artist='%s', label='%s', asin='%s' WHERE itemId=%s;" % (fields['Type'], fields['Title'], fields['ReleaseDate'], fields['Artist'], fields['Label'], fields['ASIN'], item_id)
            self.cursor.execute(query)
            self.conn.commit()
            return True

