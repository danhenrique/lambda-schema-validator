from jsonschema import ValidationError
import src.validation as validator
from src.models.lambda_response import LambdaResponse


def lambda_handler(event, context):
    """
    Handles the Lambda function invocation.

    Args:
        event (dict): The event data passed to the Lambda function.
        context (object): The context object passed to the Lambda function.

    Returns:
        dict: The response data returned by the Lambda function.
    """

    try:
        instance, schema = event['instance'], event['schema']
        validator.validate(instance, schema)
        return LambdaResponse.success(body=instance)
    except KeyError as e:
        return LambdaResponse.error(status_code=400, err=type(e).__name__, message=str(e))
    except ValidationError as e:
        return LambdaResponse.error(status_code=400, err=type(e).__name__, message=str(e))
    except Exception as e:
        return LambdaResponse.error(status_code=500, err=type(e).__name__, message='Internal Server Error')
