"""Mock for dataclasses.field() to handle description parameter."""

from dataclasses import field as dataclass_field


def field(*args, **kwargs):
    """Mock field function that removes description parameter."""
    if "description" in kwargs:
        del kwargs["description"]
    return dataclass_field(*args, **kwargs)


import dataclasses

# Replace the field function in the dataclasses module
import sys

sys.modules["dataclasses"].field = field
