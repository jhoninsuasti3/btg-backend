import os

import boto3
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")


def create_ssm_parameters(params, region_origin, ENVIRONMENT):
    ssm_client = boto3.client(
        "ssm",
        region_name=region_origin,
        aws_access_key_id=os.getenv("ENV_AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("ENV_AWS_SECRET_ACCESS_KEY"),
    )

    for param in params:
        param_name = param.get("Name")
        param_name = f"{param_name}{ENVIRONMENT}"
        description = param.get(
            "Description", f"Default value for parameter {param_name}"
        )
        value = param.get("Value", f"{param_name}Param")

        response = ssm_client.put_parameter(
            Name=param_name,
            Description=description,
            Value=value,
            Type="String",
            Overwrite=True,
        )
        print(f"Parameter '{param_name}' created with value '{value}'")


if __name__ == "__main__":
    defaults = [
        {
            "Name": "SQSBatchSizeBtgPactual",
            "Description": "Batch size for SQS",
            "Value": "10",
        },
        {
            "Name": "AuthorizerTimeoutBtgPactual",
            "Description": "Timeout for authorizer",
            "Value": "3000",
        },
        {
            "Name": "DBSuffixBtgPactual",
            "Description": "Database suffix",
            "Value": "BtgPactual",
        },
        {
            "Name": "TokenExpirationBtgPactual",
            "Description": "Token expiration time",
            "Value": "3600",
        },
        {
            "Name": "GlobalTimeoutBtgPactual",
            "Description": "Global timeout setting",
            "Value": "60",
        },
        {
            "Name": "DyanmoDBReadCapacityUnitsBtgPactual",
            "Description": "Read capacity units for DynamoDB",
            "Value": "5",
        },
        {
            "Name": "DyanmoDBWriteCapacityUnitsBtgPactual",
            "Description": "Write capacity units for DynamoDB",
            "Value": "5",
        },
        {
            "Name": "SecretKeyBtgPactual",
            "Description": "Secret key for application",
            "Value": "mysecretkey",
        },
        {
            "Name": "EnvAwsRegionBtgPactual",
            "Description": "AWS Region",
            "Value": "us-east-2",
        },
        {
            "Name": "StackNameBtgPactual",
            "Description": "Stack name",
            "Value": "stackname",
        },
        {
            "Name": "EnvBucketNameBtgPactual",
            "Description": "Bucket name",
            "Value": "bucketname",
        },
        {
            "Name": "RegionBucketBtgPactual",
            "Description": "Bucket region",
            "Value": "us-east-2",
        },
        {
            "Name": "SendGridApiKeyBtgPactual",
            "Description": "SendGrid API Key",
            "Value": "sendgridapikey",
        },
        {
            "Name": "FromEmailBtgPactual",
            "Description": "From email address",
            "Value": "fromemail@example.com",
        },
    ]
    region_origin = "us-east-1"
    ENVIRONMENT = "Develop"
    create_ssm_parameters(defaults, region_origin, ENVIRONMENT)
