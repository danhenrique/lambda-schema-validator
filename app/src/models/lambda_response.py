import json


class LambdaResponse:
    def __init__(self, status_code=200, body: dict = None, headers=None):
        self.status_code = status_code
        self.body = json.dumps(body) if body is not None else ''

        if headers is None:
            headers = {}
        headers['Content-Type'] = 'application/json'
        self.headers = headers

    @property
    def proxy_integration(self):
        return {
            'statusCode': self.status_code,
            'headers': self.headers,
            'body': self.body
        }

    @staticmethod
    def success(body=None, headers=None):
        return LambdaResponse(status_code=200, body=body, headers=headers).proxy_integration

    @staticmethod
    def error(status_code, err, message, details=None, headers=None):
        body = {
            'error': err,
            'message': message
        }
        if details:
            body['details'] = details
        return LambdaResponse(status_code=status_code, body=body, headers=headers).proxy_integration
