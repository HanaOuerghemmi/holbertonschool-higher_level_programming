#!/usr/bin/python3
""" write a file using with """

import json


def from_json_string(my_str):
    """
    function that  return the JSON  representation of an object string
    """
    return json.loads(my_str)
