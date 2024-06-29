import json
import unittest
from lambda_function import lambda_handler


class TestLambdaHandler(unittest.TestCase):
    def test_lambda_handler_valid_data(self):
        # Test case for valid data
        event = {
            'instance': {
                'name': 'John Doe',
                'age': 30
            },
            'schema': 'person'
        }
        context = {}
        response = lambda_handler(event, context)
        response_body = json.loads(response['body'])
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response_body, event['instance'])

    def test_lambda_handler_invalid_data(self):
        # Test case for invalid data
        event = {
            'instance': {
                'name': 'John Doe',
                'age': 'thirty'
            },
            'schema': 'person'
        }
        context = {}
        response = lambda_handler(event, context)
        response_body = json.loads(response['body'])
        self.assertEqual(response['statusCode'], 400)
        self.assertEqual(response_body['error'], 'ValidationError')

    def test_lambda_handler_missing_instance(self):
        # Test case for missing 'instance' key in event
        event = {
            'schema': 'person_schema'
        }
        context = {}
        response = lambda_handler(event, context)
        response_body = json.loads(response['body'])
        self.assertEqual(response['statusCode'], 400)
        self.assertEqual(response_body['error'], 'KeyError')


if __name__ == '__main__':
    unittest.main()
