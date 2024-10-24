
def insert_element(arr : list, arr2):
    arr.extend(arr2)
    return arr


arr = [22,21,42,43,53,32,51]
arr2 = [33, 44,55,66,77,88]
print(insert_element(arr, arr2))