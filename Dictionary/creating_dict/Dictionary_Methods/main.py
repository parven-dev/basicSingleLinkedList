
#clear method 

my_Dict = {"University": "University of Universe", "UID": "Space+Bound", "Aim": "Spreading Information"}

# my_Dict.clear() # will clear all the data inide dictionary

# my_Dict.copy() # make copy of original and does not contain  the original one

# fromkeys()
# this method create new dictionary from given squence of elements with value we provided
# dictionary.fromkeys(seq[], value)

# new_dict = {}.fromkeys(["a", "b", "c"], [1, 2,3])
# if this new_dict = {}.fromkeys(["a", "b", "c"]) return None or assin NOne to each 
# print(new_dict)

# get() method , this method return value for specified key if key in dict ,
# dict.get(key, value) value is optional , if key not found then value assign to key

# print(my_Dict.get("University", "stan")) # return value from dict
# print(my_Dict.get("university", "stan")) # if key not presemt in dictionary then return value that if optional



# items() method , this method doest contain any value , it return key, value pair
# print(my_Dict.items())


#keys() this method return keys
# print(my_Dict.keys())


# popitem() this method remove and return element , its dosnt contain any parameter
# print(my_Dict.popitem())


#setDefault() return value of key from dictionary if key not in dictionary it will insert, take param  key , default_value(optional)
# print(my_Dict.setdefault("University", "great"))
# print(my_Dict.setdefault("university", "great")) now return default_value, cause key not there in dictionary


#pop() remove and return element from dictionary with given key, take two param, pop(key, default_value)
# print(my_Dict.pop("university", "great")) return default_value cause key not found in dictionary
# print(my_Dict.pop("University", "great")) return exact value cause key found

 
# value() it return list that contain values, doesnt contian any  param
# print(my_Dict.values())

#update() method, this method update element of another dictinary to current dictionary if key not  found in dictinoary
# dictionary.update(other_dictionary)

new_dict = {1:"x", 2:"y", 3:"z"}
my_Dict.update(new_dict)

print(my_Dict)



