from flask_wtf import FlaskForm
from pydantic import ValidationError
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, EqualTo

from .models import PydanticAccount
from .schema import PydanticAccountSchema


class SignupForm(FlaskForm):
    email = EmailField(
        label="Email",
        name="email",
        validators=[DataRequired("The field 'email' is required.")],
        render_kw={"placeholder": "Enter your email."},
    )
    password = PasswordField(
        label="Password",
        name="password",
        validators=[DataRequired("The field 'password' is required. ")],
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

        try:
            PydanticAccountSchema(
                email=str(self.email.data),
                password=str(self.password.data),
                uuid=None,
            )
        except ValidationError as e:
            field, message = PydanticAccountSchema.process_error(e)
            self[field].errors.append(message)
            return False

        account = PydanticAccount.query.filter_by(email=self.email.data).first()

        if account:
            self.email.errors.append("The email already exists.")
            return False
        if self.password.data != self.confirm.data:
            self.password.errors.append("Passwords must match.")
            return False

        return True
