from flaskext.mysql import MySQL
from db_config import db_user, db_password, db_name, db_host


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

    def get_all(self, Class, table_name):
        res = []
        self.cursor.execute(
            "SELECT * FROM library.%s" % table_name)
        data = self.cursor.fetchall()
        args = [d[0] for d in self.cursor.description]
        for record in data:
            kwargs = {}
            for i in range(len(args)):
                kwargs[args[i]] = record[i]
            item = Class(**kwargs)
            res.append(item)
        return res


