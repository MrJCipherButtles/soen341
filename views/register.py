class Register:
    @staticmethod
    def register_user(db_gateway, request):
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
        db_gateway.cursor.execute(
            "INSERT INTO library.clients (firstName, lastName, address, email, phone) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
                fname, lname, address_1 + ' ' + address_2 + ' ' + city + ' ' + state + ' ' + postal + ' ' + country,
                email, str(phone)))
        db_gateway.conn.commit()
        return "registration successful"
