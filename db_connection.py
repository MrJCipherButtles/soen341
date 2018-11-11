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
        ids_str = "(" + str(ids)[1:len(str(ids)) - 1] + ")"
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
