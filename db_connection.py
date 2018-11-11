from flaskext.mysql import MySQL
from helper.db_config import db_user, db_password, db_name, db_host


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

    def get_all(self, Class):
        res = []
        self.cursor.execute(
            "SELECT * FROM library.items WHERE items.itemType = '%s';" % Class.__name__.upper())
        ids = [res[0] for res in self.cursor.fetchall()]
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
        fields[0] = "itemId"
        fields = self.arr_to_mysqlarr(fields).replace("'", "")
        vals = self.arr_to_mysqlarr(vals)
        query = "INSERT INTO %s %s VALUES %s;" % (self.class_to_table[type(item).__name__.upper()], fields, vals)
        print(query)
        self.cursor.execute(query)
        self.conn.commit()
