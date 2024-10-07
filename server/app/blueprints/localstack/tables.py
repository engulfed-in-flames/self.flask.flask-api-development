INVOICE_TABLE_SCHEMA = {
    "TableName": "Invoices",
    "AttributeDefinitions": [
        {
            "AttributeName": "invoice_id",
            "AttributeType": "S",
        }
    ],
    "KeySchema": [
        {
            "AttributeName": "invoice_id",
            "KeyType": "HASH",
        }
    ],
    "ProvisionedThroughput": {
        "ReadCapacityUnits": 5,
        "WriteCapacityUnits": 5,
    },
}
