from clean_dict import remove_empty  # Substitua 'seu_modulo' pelo nome do arquivo onde a função está definida.

def test_example():
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
    expected = {
        "name": "John",
        "contacts": {
            "phone": "123456789",
            "addresses": [
                {"city": "New York"}, #correct
                {"zip": "10001"}
            ]
        }
    }
    assert remove_empty(data) == expected

def test_remove_empty_basic():
    data = {
        "name": "John",
        "age": None,
        "email": "",
        "phone": "123456789",
        "tags": []
    }
    expected = {
        "name": "John",
        "phone": "123456789"
    }
    assert remove_empty(data) == expected

def test_remove_empty_nested():
    data = {
        "user": {
            "name": "Alice",
            "contacts": {
                "email": "",
                "phone": None,
                "address": {"city": "", "zip": "12345"}
            }
        },
        "preferences": {},
        "tags": []
    }
    expected = {
        "user": {
            "name": "Alice",
            "contacts": {
                "address": {"zip": "12345"}
            }
        }
    }
    assert remove_empty(data) == expected

def test_remove_empty_list():
    data = ["", None, [], {}, "Valid", ["", "Nested", {}]]
    expected = ["Valid", ["Nested"]]
    assert remove_empty(data) == expected

def test_remove_empty_only_empty():
    data = {"a": "", "b": None, "c": [], "d": {}}
    expected = {}
    assert remove_empty(data) == expected

def test_remove_empty_mixed_types():
    data = {
        "count": 0,
        "flag": False,
        "empty_str": "",
        "empty_list": [],
        "empty_dict": {}
    }
    expected = {
        "count": 0,
        "flag": False
    }
    assert remove_empty(data) == expected
