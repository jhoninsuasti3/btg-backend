""" Authorizer DB to Dynamo """

import os
from functools import reduce
from operator import and_

import boto3
from boto3.dynamodb.conditions import Attr


class AwsDynamo:
    """
    Esta clase proporciona métodos para interactuar con la base de datos DynamoDB.
    """

    def __init__(self, test_env_prefix="test"):
        """
        Inicializa la clase DynamoDB y establece la conexión con la base de datos DynamoDB según el entorno.
        """
        if test_env_prefix in os.environ.get("ENVIRONMENT", "").lower():
            from moto import mock_aws  # pylint: disable=C0415

            mocking = mock_aws()
            mocking.start()
            self.dynamodb = boto3.resource("dynamodb", region_name="us-west-2")
        elif "local" in os.environ.get("ENVIRONMENT"):
            self.dynamodb = boto3.resource(
                "dynamodb",
                aws_access_key_id=os.environ.get("ENV_AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=os.environ.get("ENV_AWS_SECRET_ACCESS_KEY"),
                region_name=os.environ.get("ENV_AWS_REGION"),
            )
        else:
            self.dynamodb = boto3.resource(
                "dynamodb",
            )

    def build_query_params(self, filters):
        """
        Construye los parámetros de consulta basados en los filtros proporcionados.

        :param filters: Los filtros para la consulta.
        :type filters: dict
        :return: Los parámetros de consulta construidos.
        :rtype: dict
        """
        query_params = {}
        if len(filters) > 0:
            query_params["FilterExpression"] = self.add_expressions(filters)
        return query_params

    def add_expressions(self, filters: dict):
        """
        Construye expresiones de filtro para la consulta.

        :param filters: Los filtros para la consulta.
        :type filters: dict
        :return: La expresión de filtro construida.
        :rtype: Attr or None
        """
        if filters:
            conditions = []
            for key, value in filters.items():
                if isinstance(value, int):
                    conditions.append(Attr(key).eq(value))
            return reduce(and_, conditions)
        return None


class DB(AwsDynamo):
    """
    Esta clase se utiliza para interactuar con una base de datos DynamoDB en el contexto de autenticación y generación
    de tokens.
    """

    def __init__(self, dynamo_table, test_env_prefix="test"):
        """
        Inicializa la clase DB y establece la conexión con la base de datos DynamoDB.
        """
        super().__init__(test_env_prefix)

        self.dynamo_table = dynamo_table
        self.table = self.dynamodb.Table(dynamo_table)
        if test_env_prefix in os.environ.get("ENVIRONMENT", "").lower():
            self.create_test_tables()

    def create_test_tables(self):
        """
        Creacion de tablas para el caso de pruebas,
        por defecto se crea con un parametro uuid.
        Es posible sobreescribir este metodo para crear tablas
        con otros parametros.
        """
        try:
            self.dynamodb.create_table(
                TableName=self.table,
                KeySchema=[{"AttributeName": "uuid", "KeyType": "HASH"}],
                AttributeDefinitions=[{"AttributeName": "uuid", "AttributeType": "S"}],
                ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
            )
        except Exception:
            return

    def get_item_by_uuid(self, uuid):
        """
        Obtiene un elemento de la tabla por su UUID.

        :param uuid: El UUID del elemento que se va a buscar.
        :type uuid: str
        :return: El ID de usuario asociado al UUID si se encuentra, de lo contrario, None.
        :rtype: str or None
        """
        try:
            token_exist = self.table.get_item(Key={"uuid": uuid}).get("Item")
            return token_exist

        except Exception as e:
            print("Error DynamoDB get_item_by_token: {}".format(str(e)))
            return None

    def put_item_data(self, data):
        """
        Inserta un nuevo elemento en la tabla.

        :param data: Los datos del elemento que se va a insertar.
        :type data: dict
        :return: El resultado de la operación de inserción.
        """
        try:
            return self.table.put_item(Item=data)
        except Exception as e:
            print("Error DynamoDB put_item_data: {}".format(str(e)))
            raise e


class AuthorizerDB(DB):
    """
    Authorizer DB
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__(os.getenv("AUTHORIZER_TABLE"))
