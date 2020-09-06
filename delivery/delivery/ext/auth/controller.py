from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename

from flask import current_app as app

from delivery.ext.auth.models import User
from delivery.ext.db import db
import os

ALG = "pbkdf2:sha256"

def create_user(email, password, admin=False):
    user = User(
        email=email, 
        passwd=generate_password_hash(password, ALG),
        admin = admin,
    )

    db.session.add(user)
    # TODO: Tratar exception caso o usuario já exista
    db.session.commit()
    return user

def save_user_foto(filename, filestorage):
    """
        Save user foto in ./uploads/foo/asdad.ext 
    """
    filename = os.path.join(
        app.config["UPLOAD_FOLDER"],
        secure_filename(filename)
    )
    # TODO: 1) verificar se o diretório existe, 2) criar se não existir
    filestorage.save(filename)
