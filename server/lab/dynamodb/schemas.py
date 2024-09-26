USER_TABLE_SCHEMA = {
    "TableName": "User",
    "AttributeDefinitions": [
        {"AttributeName": "email", "AttributeType": "S"},
        {"AttributeName": "name", "AttributeType": "S"},
    ],
    "KeySchema": [
        {"AttributeName": "email", "KeyType": "HASH"},
        {"AttributeName": "name", "KeyType": "RANGE"},
    ],
    "ProvisionedThroughput": {
        "ReadCapacityUnits": 5,
        "WriteCapacityUnits": 5,
    },
}
