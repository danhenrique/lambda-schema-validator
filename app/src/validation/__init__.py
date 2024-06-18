r"""
"""
__version__ = '0.0.1'
__author__ = 'DanHenrique'

__all__ = []

import importlib
from jsonschema import validate as validate_schema
from . import schemas_definitions as defs

schemas = defs.schemas


def _get_schema(n):
    if n in schemas:
        module = importlib.import_module(schemas[n.lower()], __name__)
        return module.schema
    else:
        raise ValueError(f"Schema {n} not found.")


def validate(data, schema_name):
    schema = _get_schema(schema_name)
    validate_schema(data, schema)
