
def insert_element(arr, index):
    arr.insert(index, 300)
    return arr


arr = [22,21,42,43,53,32,51]
index = 5
print(insert_element(arr, index))