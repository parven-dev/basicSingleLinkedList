

def searching_value(dictionary: dict, value:int):
    for key in dictionary:
        if dictionary[key] == value:
            return f"value found: {dictionary[key]}"



dictionary = {"one": 1, "two": 2, "three": 3, "four": 4}
value = 3

print(searching_value(dictionary, value))