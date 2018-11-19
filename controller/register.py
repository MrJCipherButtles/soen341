from flask import redirect, url_for, request

from controller.controller import Controller


class Register(Controller):
    def register_user(self):
        self.db.register_user(request)
        return redirect(url_for('login'))

  #Implement a failure login view if the registration popped up an error (discuss with team)
    def register_user_admin(self):
        self.db.register_user_admin(request)
        return redirect(url_for('successLogin'))
      #I redirect to the login page. Othrewise, the login page will be
    # rendered within the navguaion bar and side bars which creates a nested view (bad design)
