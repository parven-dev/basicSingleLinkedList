from array import array 

my_array = array('i', [1,2,3,4,5])
print(my_array, "before insertion ")

my_array.insert(1, 4)
print(my_array, "after insertion")