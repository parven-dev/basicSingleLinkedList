

def accessing_elements(array, index):
    if index >= len(array):
        return "there is not index  in this given array"
    else:
        return array[index]



array = ["i", 1,2,3,4,5,6,7,8,9,10]
index = 4
print(accessing_elements(array=array, index=index))