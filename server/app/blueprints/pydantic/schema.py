from typing import Annotated, Any

from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    ValidationInfo,
    ValidatorFunctionWrapHandler,
    WrapValidator,
)

ERROR_MESSAGES: dict[str, str] = {
    "email": "The given email is invalid.",
    "password": "The given password is invalid.",
    "uuid": "",
}


def invalid_to_none(
    value: Any, handler: ValidatorFunctionWrapHandler, info: ValidationInfo
) -> str | None:
    try:
        return handler(value)
    except ValidationError:
        return None


type Ignored = Annotated[str | None, WrapValidator(invalid_to_none)]


class PydanticAccountSchema(BaseModel):
    uuid: Ignored
    email: str = Field(
        title="email",
        pattern=r"^[a-zA-Z0-9]+@cal\.test\.co\.jp$",
        frozen=True,
        strict=True,
    )
    password: str = Field(
        title="password",
        pattern=r"^[A-Za-z\d@$!%*#?&]{8,}$",
        frozen=True,
        strict=True,
        exclude=True,
    )

    @classmethod
    def process_error(cls, validation_error: ValidationError) -> tuple[str, str]:
        error = validation_error.errors()[0]
        field = str(error["loc"][0])
        message = ERROR_MESSAGES[field]
        return field, message
