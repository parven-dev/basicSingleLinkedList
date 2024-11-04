def inserting_value(dictionary: dict, value: int):
    dictionary["count"] = value

    return dictionary

dictionary = {"a": "apple", "b": "Ball", "c": "Cat"}
value = 3

print(inserting_value(dictionary, value))