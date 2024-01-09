#!/usr/bin/python3
"""to_json_string function"""
import json


def to_json_string(my_obj):
    """
    Change object to json
    Args:
        my_object (objec): object to change
    Returns:
        json object.
    """
    return json.dumps(my_obj)
