def is_empty(v):
    return v in [None, "", [], {}]

def remove_empty(data):
    if isinstance(data, dict):
        cleaned_dict = {}
        for k, v in data.items():
            cleaned_key = remove_empty(k)
            cleaned_value = remove_empty(v)
            if (not is_empty(cleaned_key)) and (not is_empty(cleaned_value)):
                cleaned_dict[cleaned_key] = cleaned_value
        return cleaned_dict
    
    elif isinstance(data, list):
        cleaned_list = []
        for v in data:
            cleaned_value = remove_empty(v)
            if not is_empty(cleaned_value):
                cleaned_list.append(cleaned_value)
        return cleaned_list
    
    elif isinstance(data, str):
        data = data.strip()

    return data


# data = {
#     "name": "John",
#     "age": None,
#     "contacts": {
#         "email": "",
#         "phone": "123456789",
#         "addresses": [
#             {"city": "New York", "zip": ""},
#             {},
#             {"city": "", "zip": "10001"}
#         ]
#     },
#     "tags": []
# }

# data_cleaned = remove_empty(data)
# print(data_cleaned)