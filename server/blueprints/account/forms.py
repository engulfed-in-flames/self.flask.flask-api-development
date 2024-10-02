from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

from .models import User


class SignupForm(FlaskForm):
    email = EmailField(
        label="Email",
        name="email",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter your email."},
    )
    password = PasswordField(
        label="Password",
        name="password",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter your password."},
    )
    confirm = PasswordField(
        label="Confirm password",
        name="confirm-password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
        render_kw={"placeholder": "Confirm your password."},
    )

    def validate(self, extra_validators=None):
        initial_validation = super(SignupForm, self).validate()
        if not initial_validation:
            return False

        user = User.query.filter_by(email=self.email.data).first()
        if user and isinstance(self.email.errors, list):
            self.email.errors.append("The email already exists.")
            return False
        if (self.password.data != self.confirm.data) and isinstance(self.password.errors, list):
            self.password.errors.append("Passwords must match.")
            return False
        return True


class LoginForm(FlaskForm):
    email = StringField(
        label="Email",
        name="email",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter your email."},
    )
    password = PasswordField(
        label="Password",
        name="password",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter your password."},
    )
