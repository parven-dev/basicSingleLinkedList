def find_missing_number(arr):
    
    sum_of_all = 0
    for num in arr:
        sum_of_all+=num
        
    result = 5050 - sum_of_all 
    return result

arr = []
for item in range(1, 100+1):
    arr.append(item)

arr.remove(74)

print(find_missing_number(arr))