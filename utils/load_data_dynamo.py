import boto3
import os
from botocore.exceptions import ClientError
from shared_package.constants import EnvironmentVariables


client_dynamo = boto3.resource(
    "dynamodb",
    aws_access_key_id=EnvironmentVariables.ENV_AWS_ACCESS_KEY_ID,
    aws_secret_access_key=EnvironmentVariables.ENV_AWS_SECRET_ACCESS_KEY,
    region_name=EnvironmentVariables.ENV_AWS_REGION,
)

table_fund = client_dynamo.Table(EnvironmentVariables.FOUNDS_TABLE_NAME)

# Lista de datos que deseas insertar
funds_to_insert = [
    {
        "uuid": "b220c615-dc09-4770-b234-1c771baf2154",
        "name": "FPV_BTG_PACTUAL_RECAUDADORA",
        "min_amount": 75000,
        "category": "FPV",
    },
    {
        "uuid": "4d77cee7-c9e4-42cc-be9b-528616d38bca",
        "name": "FPV_BTG_PACTUAL_ECOPETROL",
        "min_amount": 125000,
        "category": "FPV",
    },
    {
        "uuid": "c26385e6-8014-4f08-86bc-e945da3d016a",
        "name": "DEUDAPRIVADA",
        "min_amount": 50000,
        "category": "FIC",
    },
    {
        "uuid": "3df7b7ff-8666-4b77-aae5-6f4a1e70c75f",
        "name": "FDO-ACCIONES",
        "min_amount": 250000,
        "category": "FIC",
    },
    {
        "uuid": "f01d6410-794d-4064-9dec-26a59b9c0059",
        "name": "FPV_BTG_PACTUAL_DINAMICA",
        "min_amount": 100000,
        "category": "FPV",
    },
]


def insert_funds(funds):
    for fund in funds:
        try:
            response = table_fund.put_item(Item=fund)
            print(f"Datos insertados con éxito para UUID: {fund['uuid']}")
        except ClientError as e:
            print(f"Error al insertar datos para UUID: {fund['uuid']}: {str(e)}")


insert_funds(funds_to_insert)
