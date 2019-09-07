"""This file provides the implementation for the /example_endpoint API endpoint"""

def search():
    """This is called when someone does a GET request with no parameters to /example_endpoint"""
    data = [
        {"name": "first_key", "value": "string one"},
        {"name": "second_key", "value": "string two"},
    ]
    return data