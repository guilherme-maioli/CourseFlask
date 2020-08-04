from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from flask_admin.contrib.sqla import filters
from delivery.ext.auth.models import User
from delivery.ext.db import db
from flask import flash

#def format_user(self, request, user, *args):
#    return user.email.split("@")[0]

# TODO: descrever todos os modos


class UserAdmin(ModelView):
    """ Interface admin de user """
    column_formatters = {
        "email": lambda s, r, u, *a: u.email.split("@")[0]
    }

    column_list = ["email", "admin"]

    column_searchable_list = ['email']

    column_filters = [
        'email', 
        'admin',
        filters.FilterLike(
            User.email,
            "dominio",
            options=(("gmail", "Gmail"), ("uol", "UOL"))
        )
        ]


    can_edit = False
    can_create = True
    can_delete = True

    @action(
        'toggle_admin',
        'Toggle admin status',
        'Are you sure?' 
    )
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f"{len(users)} usuários alterados com sucesso!", "sucess")

    @action(
        'send_email',
        'Send email to all users',
        'Are you sure?' 
    )
    def send_email(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        flash(f"{len(users)} emails enviados.", "sucess")

