import numpy as np

twoDArray = np.array([[22,33,44,55,66], [21, 32, 43, 54,65], [12,13,14,15,16],[ 21, 31, 41, 51,61]])
print(twoDArray)


# insert 

newArray = np.insert(twoDArray, 0, [[99, 88, 77, 66, 55]], axis=0) 
# it will add columns wise
# 1 axis means columns , 0 axis means row 
# 0 (means first row , if axis is 1 , 0 means firt column) means position row or column 
print( newArray)
