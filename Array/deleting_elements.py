

from array import array

def deleting_elements(arr, value):
    if value in arr:
        arr.remove(value)
        return arr
    else:
        print("value not found")

arr = array("i", [2,3,4,5,6,7,8])
value = 4
print(deleting_elements(arr, value))