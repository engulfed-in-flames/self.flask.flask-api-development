from typing import TypedDict


class DynamoResponseMetadata(TypedDict, total=False):
    RequestId: str
    HTTPStausCode: int
    HTTPHeaders: dict[str, str]
    RetryAttempts: int


class DynamoGetItemResponse(TypedDict, total=False):
    Item: dict[str, dict[str, str]] | None
    ResponseMetadata: DynamoResponseMetadata


class UserType(TypedDict):
    email: str
    name: str
