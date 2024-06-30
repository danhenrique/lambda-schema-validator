r"""
"""
__version__ = '0.0.1'
__author__ = 'DanHenrique'

__all__ = []

from jsonschema import validate as validate_schema
# Schemas definitions
from .schemas import person
from .schemas import product


def _get_schema(n):
    if n == 'person':
        return person.schema
    elif n == 'product':
        return product.schema
    else:
        raise ValueError(f"Schema {n} not found.")


def validate(data, schema_name):
    schema = _get_schema(schema_name)
    validate_schema(data, schema)
