from flask import request
import datetime

class Loan:
    @staticmethod
    def loan_item(db_gateway):
        user = request.cookies.get('username')
        itemID = request.form['itemID']



        db_gateway.cursor.execute(
            "INSERT INTO library.loans (clientId, itemId, loan_date) VALUES ('%s', '%s', '%s')" % (
                user, itemID, datetime.datetime.today().strftime('%Y-%m-%d')))
        db_gateway.conn.commit()
        return "loan successful"
