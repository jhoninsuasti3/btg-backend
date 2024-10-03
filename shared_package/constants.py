import os
import boto3


class EnvironmentVariables:
    """Class for the environment variables."""

    SECRET_API_KEY: str = os.getenv("SECRET_API_KEY", "")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    TOKEN_API_EXPIRATION: int = int(os.getenv("TOKEN_API_EXPIRATION", 0))
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "local")
    DEBUG = os.getenv("DEBUG")
    ENV_BUCKET_NAME: str = os.getenv("ENV_BUCKET_NAME", "")
    ENV_AWS_ACCESS_KEY_ID: str = os.getenv("ENV_AWS_ACCESS_KEY_ID", "")
    ENV_AWS_SECRET_ACCESS_KEY: str = os.getenv("ENV_AWS_SECRET_ACCESS_KEY", "")
    ENV_AWS_REGION: str = os.getenv("ENV_AWS_REGION", "")
    FOUNDS_TABLE_NAME: str = os.getenv("FOUNDS_TABLE_NAME", "")
    TRANSACTIONS_TABLE_NAME: str = os.getenv("TRANSACTIONS_TABLE_NAME", "")
    USERS_TABLE_NAME: str = os.getenv("USERS_TABLE_NAME", "")


if EnvironmentVariables.ENVIRONMENT.lower() in ["test", "local"]:
    client_dynamo = boto3.resource(
        "dynamodb",
        aws_access_key_id=EnvironmentVariables.ENV_AWS_ACCESS_KEY_ID,
        aws_secret_access_key=EnvironmentVariables.ENV_AWS_SECRET_ACCESS_KEY,
        region_name=EnvironmentVariables.ENV_AWS_REGION,
    )
else:
    client_dynamo = boto3.resource(
        "dynamodb",
        region_name=EnvironmentVariables.ENV_AWS_REGION,
    )
