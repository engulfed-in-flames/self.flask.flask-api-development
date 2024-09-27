"""
ローカル環境で開発を進める際に、Boto3ライブラリを用いてAmazon DynamoDBとの連携をシミュレートし、
その動作を確認することを目的とします。

- Table Name: User
- Primary Key:
    - Partition Key: email (String)
    - Sort Key: name (String)
- Provisioned Throughput:
    - Read Capacity Units: 5
    - Write Capacity Units: 5

注意:
- この関数は、ローカル開発とテスト用にダミーの資格情報を使用しています。
- 本番環境では、実際の資格情報に置き換える必要があります。
"""

import boto3
import boto3.session

from .schemas import USER_TABLE_SCHEMA
from .credentials import BOTO3_SESSION_CONFIG, BOTO3_CLIENT_CONFIG
from .models import UserDTO

RESOURCE = "dynamodb"


session = boto3.session.Session(**BOTO3_SESSION_CONFIG)
client = session.client(RESOURCE, **BOTO3_CLIENT_CONFIG)

table_name = "User"


def create_user_table() -> None:
    existing_tables = client.list_tables()["TableNames"]

    if table_name not in existing_tables:
        response = client.create_table(**USER_TABLE_SCHEMA)

        print(table_name, " table is created: ", response)


def create_user(user) -> None:
    response = client.put_item(
        TableName=table_name,
        Item={
            "email": {"S": user.get("email")},
            "name": {"S": user.get("name")},
        },
    )

    print("A user is created: ", response)


def find_user() -> None:
    response = client.get_item(
        TableName=table_name,
        Key={
            "email": {"S": "user1@example.com"},
            "name": {"S": "mario"},
        },
    )

    user = response.get("Item")

    deserialized = UserDTO.deserialize(user)
    serialized = UserDTO.serialize(deserialized)

    print(deserialized)
    print(serialized)
