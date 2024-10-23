import numpy as np

def accesing_elements(arr, row_index, col_index):
    if  row_index >= len(arr) or col_index >= len(arr):
        return "index out of range"
    
    else:
        print(arr[row_index][col_index])

twoDArray = np.array([[22,33,44,55,66], [21, 32, 43, 54,65], [12,13,14,15,16],[ 21, 31, 41, 51,61]])
row_index = 3
col_index  = 2
print(accesing_elements(arr=twoDArray, row_index=row_index, col_index=col_index))

