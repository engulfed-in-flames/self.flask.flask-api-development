from dataclasses import dataclass

from boto3.dynamodb.types import TypeDeserializer, TypeSerializer


class DynamoDTO:

    @classmethod
    def serialize(cls, python_object: dict) -> dict:
        ts = TypeSerializer()

        return {k: ts.serialize(v) for k, v in python_object.items()}

    @classmethod
    def deserialize(cls, dynamo_object: dict) -> dict:
        td = TypeDeserializer()

        return {k: td.deserialize(v) for k, v in dynamo_object.items()}


@dataclass(frozen=True)
class UserDTO(DynamoDTO):
    email: str
    name: str
