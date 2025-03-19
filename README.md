First challenge

Part 1: Recursive Dictionary Cleanup

Task Description

Write a Python function that recursively removes all empty values (such as None, empty strings "", empty lists [], and empty dictionaries {}) from a nested dictionary structure.

Requirements

    •    The function should recursively traverse the dictionary and its nested children.
    •    Empty values should be removed entirely from the dictionary.
    •    The function should handle deeply nested structures.

Example Input & Output

Input:

data = {
    "name": "John",
    "age": None,
    "contacts": {
        "email": "",
        "phone": "123456789",
        "addresses": [
            {"city": "New York", "zip": ""},
            {},
            {"city": "", "zip": "10001"}
        ]
    },
    "tags": []
}

Expected Output:

{
    "name": "John",
    "contacts": {
        "phone": "123456789",
        "addresses": [
            {"city": "New York"}, #correct
            {"zip": "10001"}
        ]
    }
}

Deliverables

    •    A Python script (clean_dict.py) that implements this function.
    •    Unit tests to validate the implementation.


Solution:

I created a simple function that recursively checks the type of the data and whether it is empty. If the data is empty, it is not saved.

To run the tests, follow these steps:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests -vv

