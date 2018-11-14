from flask import redirect, url_for


class Register:
    @staticmethod
    def register_user(db_gateway, request):
        db_gateway.register_user(request)
        return redirect(url_for('login'))

    @staticmethod
    def register_user_admin(db_gateway, request):
        db_gateway.register_user_admin(request)
        return redirect(url_for('login'))
