import numpy as np


def find_maximum_product(arr):
    sorted_array  = sorted(arr)
    return sorted_array[-1] * sorted_array[-2]


myArray = np.array([1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21])

# print(find_maximum_product(myArray))


def find_maximum_product2(arr):
    maximu_product = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] > maximu_product:
                maximu_product = arr[i] * arr[j]
    
    return maximu_product   


myArray = np.array([1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21])
print(find_maximum_product2(myArray))