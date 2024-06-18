schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'title': 'Product',
    'description': 'A product in the catalog',
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string'
        },
        'age': {
            'type': 'integer'
        }
    },
    'required': ['name', 'age']
}
