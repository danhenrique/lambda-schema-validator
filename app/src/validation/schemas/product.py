schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'title': 'Product',
    'description': 'A product in the catalog',
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string'
        },
        'detail': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string'
                },
                'description': {
                    'type': 'string'
                }
            },
            'required': ['name', 'description']
        },
        'sku': {
            'type': 'string'
        },
        'price': {
            'type': 'number'
        },
        'cost': {
            'type': 'number'
        },
        'shipment': {
            'type': 'object',
            'properties': {
                'height': {
                    'type': 'string'
                },
                'width': {
                    'type': 'string'
                },
                'length': {
                    'type': 'string'
                },
                'weight': {
                    'type': 'string'
                },
                'diameter': {
                    'type': 'string'
                }
            },
            'required': ['height', 'width', 'length', 'weight']
        },
        'news': {
            'type': 'object',
            'properties': {
                'startDate': {
                    'type': 'string'
                },
                'endDate': {
                    'type': 'string'
                }
            },
            'required': ['height', 'width', 'length', 'weight']
        },
        'promotion': {
            'type': 'object',
            'properties': {
                'price': {
                    'type': 'number'
                },
                'startDate': {
                    'type': 'string'
                },
                'endDate': {
                    'type': 'string'
                }
            },
            'required': ['price']
        },
        'meta': {
            'type': 'object',
            'properties': {
                'title': {
                    'type': 'string'
                },
                'description': {
                    'type': 'string'
                },
                'keywords': {
                    'type': 'array',
                    'items': {
                        'type': 'string'
                    }
                }
            },
            'required': ['title', 'description']
        },
        'category': {
            'type': 'string'
        },
        'subcategory': {
            'type': 'string'
        },
        'group': {
            'type': 'string'
        }
    },
    'required': ['id', 'detail', 'price', 'shipment', 'meta', 'category', 'subcategory']
}
