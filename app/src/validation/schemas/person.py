schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'title': 'Person',
    'description': 'A person',
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
