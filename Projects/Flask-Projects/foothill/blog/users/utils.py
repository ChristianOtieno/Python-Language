import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from blog import mail


def SavePicture(form_picture):
    RandomHex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = RandomHex + f_ext
    PicturePath = os.path.join(
        current_app.root_path, 'static/ProfilePics', picture_fn)

    OutputSize = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(OutputSize)
    i.save(PicturePath)

    return picture_fn


def SendResetEmail(user):
    token = user.get_ResetToken()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
