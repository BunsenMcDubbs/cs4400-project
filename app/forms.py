from flask_wtf import FlaskForm as Form
from wtforms import TextField, PasswordField
from wtforms import validators

from .models import User

class LoginForm(Form):
    username = TextField(u'username', validators=[validators.required()])
    password = PasswordField(u'password', validators=[validators.required()])

    def validate(self):
        if not super(LoginForm, self).validate():
            return False
        user = User.find_by_username(self.username.data)
        if not user:
            self.username.errors.append('Invalid username or password')
            return False
        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid username or password')
            return False
        return True

class RegisterUserForm(Form):
    username = TextField(u'username', validators=[validators.required()])
    email = TextField(u'email', validators=[validators.required()])
    password = PasswordField(u'password', validators=[validators.required()])

    confirm_password = PasswordField(u'confirm_password', validators=[validators.required()])

    def validate(self):
        if not super(RegisterUserForm, self).validate():
            return False
        if self.password.data != self.confirm_password.data:
            self.password.errors.append('Passwords do not match')
            return False
        user = User.find_by_username(self.username.data)
        if user:
            self.username.errors.append('Username already in use')
            return False
        return True
