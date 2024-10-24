def pop_delete_remove(arr: list):
    
    # arr.pop() # remove value from the end 
    # print(arr)
    
    # arr.pop(3) # remove value from given index
    # print(arr)
    
    del arr[3:4] # delete value from targeted index
    print(arr)
    
    arr.remove(42) # remove from given value
    return arr
    
arr = [22,21,42,43,53,32,51]
print(pop_delete_remove(arr))