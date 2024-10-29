import numpy as np

def findNumber(arr, num):
    for number in range(len(arr)):
        if arr[number] == num:
            return "yes exist"
    


arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20])
num = 10

print(findNumber(arr, num))