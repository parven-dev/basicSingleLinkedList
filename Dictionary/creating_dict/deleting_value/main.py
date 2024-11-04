

def deleting_value(dictionary: dict):
    # firt pop() method
    # dictionary.pop(value) # will return deleted value
    
    # second popItem()  this will remove random value and return deleted key, value
    # dictionary.popitem()
    
    # del this can delete single value as well as whole dict
    
    # del dictionary["banana"]
    # del dictionary () # this will delete whole dict
    
    dictionary.clear() # wipe out dict
    return dictionary


dictionary = {"apple": 2, "banana": 3, "guava": 4}
# value = "guava"
print(deleting_value(dictionary))