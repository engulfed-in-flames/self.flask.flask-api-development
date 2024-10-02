import random
import boto3
from datetime import datetime
from decimal import Decimal
from flask import render_template
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer
from botocore.exceptions import ClientError

from . import localstack_bp
from .schemas import INVOICE_TABLE_SCHEMA

# from .models import Invoice

aws_region = "ap-northeast-1"

# 1. Create a session using the localstack endpoint
s3_client = boto3.client(
    service_name="s3",
    aws_access_key_id="dummyaccesskey",
    aws_secret_access_key="dummysecretkey",
    region_name=aws_region,
    endpoint_url="http://localhost:4566",
)

dynamodb_client = boto3.client(
    service_name="dynamodb",
    aws_access_key_id="dummyaccesskey",
    aws_secret_access_key="dummysecretkey",
    region_name=aws_region,
    endpoint_url="http://localhost:4566",
)


def serialize(python_object: dict) -> dict:
    ts = TypeSerializer()

    return {k: ts.serialize(v) for k, v in python_object.items()}


def deserialize(dynamo_object: dict) -> dict:
    td = TypeDeserializer()

    return {k: td.deserialize(v) for k, v in dynamo_object.items()}


@localstack_bp.route("/create-s3-buckets", methods=["GET"])
def create_s3_buckets():
    # 2. Create new buckets
    bucket_name_invoices = "invoices"
    bucket_name_config = "invoices-config"

    try:
        s3_client.create_bucket(
            Bucket=bucket_name_invoices,
            CreateBucketConfiguration={"LocationConstraint": aws_region},
        )
        s3_client.create_bucket(
            Bucket=bucket_name_config,
            CreateBucketConfiguration={"LocationConstraint": aws_region},
        )

        return "Buckets are created."
    except ClientError as e:
        return "ClientError: " + str(e)
    except Exception as e:
        return "Exception: " + str(e)


@localstack_bp.route("/list-s3-buckets", methods=["GET"])
def list_s3_buckets():
    try:
        response: dict = s3_client.list_buckets()
        buckets = [
            {
                "name": bucket["Name"],
                "created_at": bucket["CreationDate"],
            }
            for bucket in response.get("Buckets", [])
        ]

        return render_template("localstack/list.html", buckets=buckets)
    except ClientError as e:
        return "ClientError: " + str(e)
    except Exception as e:
        return "Exception: " + str(e)


@localstack_bp.route("/create-dynamodb-table", methods=["GET"])
def create_dynamodb_table():
    try:
        table_name = "invoices"
        existing_tables = dynamodb_client.list_tables()["TableNames"]

        if table_name not in existing_tables:
            response = dynamodb_client.create_table(**INVOICE_TABLE_SCHEMA)

            waiter = dynamodb_client.get_waiter("table_exists")
            waiter.wait(TableName="Invoices")

            return "The 'Invoices' table is created."

    except ClientError as e:
        return "ClientError: " + str(e)
    except Exception as e:
        return "Exception: " + str(e)


@localstack_bp.route("/create-random-invoice", methods=["GET"])
def create_random_invoice():
    try:
        table_name = "invoices"

        invoice = {
            "invoice_id": f"INVOICE{random.randint(1, 99999999):010d}",
            "customer_id": f"CUSTOMER{random.randint(1, 99999999):010d}",
            "total_amount": Decimal(round(random.uniform(25, 100), 2)),
            "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        }

        response = dynamodb_client.put_item(
            TableName=table_name,
            Item=serialize(invoice),
        )

        return "The invoice is created."

    except ClientError as e:
        return "ClientError: " + str(e)
    except Exception as e:
        return "Exception: " + str(e)


# @localstack_bp.route("/list-invoices", methods=["GET"])
# def find_invoice():
#     try:
#         table_name = "invoices"

#         invoice = {
#             "invoice_id": f"INVOICE{random.randint(1, 99999999):010d}",
#             "customer_id": f"CUSTOMER{random.randint(1, 99999999):010d}",
#             "total_amount": Decimal(round(random.uniform(25, 100), 2)),
#             "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
#         }

#         response = dynamodb_client.put_item(
#             TableName=table_name,
#             Item=serialize(invoice),
#         )

#         return "The invoice is created."

#     except ClientError as e:
#         return "ClientError: " + str(e)
#     except Exception as e:
#         return "Exception: " + str(e)
