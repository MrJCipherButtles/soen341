from flask import redirect, url_for


class Register:
    @staticmethod
    def register_user(db_gateway, request):
        db_gateway.register_user(request)
        return redirect(url_for('login'))

    @staticmethod
    def register_user_admin(db_gateway, request):
        db_gateway.register_user_admin(request)
        return redirect(url_for('http://127.0.0.1:5000/login'))
      #I redirect to the login page. Othrewise, the login page will be
    # rendered within the navguaion bar and side bars which creates a nested view (bad design)
