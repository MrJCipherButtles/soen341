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
