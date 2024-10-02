"""
Este módulo contiene funciones de utilidad para el módulo authorizer.
"""

from lib_authorizer.db import AuthorizerDB as DB


def validate_token(token, methodArn=None):
    """
    Valida un token de autorización utilizando una instancia de la clase DB.

    :param token: El token de autorización a validar.
    :type token: str
    :param methodArn: El recurso de Amazon API Gateway.
    :type methodArn: str or None
    :return: El ID de usuario asociado al token si es válido, de lo contrario, None.
    :rtype: str or None
    """
    try:
        db = DB()
        return db.get_item_by_uuid(token)
    except Exception as e:
        print("Error in validate_token: ", e)
        return None


def generate_policy(principal_id, effect, data=None):
    """
    Genera una política de autorización para un recurso de Amazon API Gateway.

    :param principal_id: El ID del principal (usuario) al que se aplica la política.
    :type principal_id: str
    :param effect: El efecto de la política (Allow o Deny).
    :type effect: str
    :param data: Datos adicionales que se agregarán al contexto de la política.
    :type data: dict or None
    :return: La política de autorización generada.
    :rtype: dict
    """
    auth_response = {}
    auth_response["principalId"] = principal_id
    policy_document = {}
    policy_document["Version"] = "2012-10-17"
    policy_document["Statement"] = []
    statement_one = {}
    statement_one["Action"] = "execute-api:Invoke"
    statement_one["Effect"] = effect
    statement_one["Resource"] = "*"
    policy_document["Statement"].append(statement_one)
    auth_response["policyDocument"] = policy_document
    auth_response["context"] = data or {}

    # print("*" * 100)
    # print(">>> Auth response: ", auth_response)
    return auth_response
