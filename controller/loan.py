from flask import request

class Loan:
    @staticmethod
    def loan_item(db_gateway, request1):
        user = request.cookies.get('username')
        itemID = request.form['itemID']



        db_gateway.cursor.execute(
            "INSERT INTO library.loans (clientId, itemId, loan_date) VALUES ('%s', '%s', '%s')" % (
                user, itemID, '2017-01-01'))
        db_gateway.conn.commit()
        return "loan successful"
