AWS_ACCESS_KEY_ID = "dummyaccesskey"
AWS_SECRET_ACCESS_KEY = "dummysecretkey"
AWS_SESSION_TOKEN = "dummysessiontoken"
AWS_REGION_NAME = "ap-northeast-1"
AWS_ENDPOINT_URL = "http://localhost:8000"

BOTO3_SESSION_CONFIG = {
    "aws_access_key_id": AWS_ACCESS_KEY_ID,
    "aws_secret_access_key": AWS_SECRET_ACCESS_KEY,
    "aws_session_token": AWS_SESSION_TOKEN,
    "region_name": AWS_REGION_NAME,
}

BOTO3_CLIENT_CONFIG = {
    "aws_access_key_id": AWS_ACCESS_KEY_ID,
    "aws_secret_access_key": AWS_SECRET_ACCESS_KEY,
    "endpoint_url": AWS_ENDPOINT_URL,
    "verify": False,
}
