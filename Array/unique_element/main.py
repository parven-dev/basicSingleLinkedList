

def all_unique(arr : list):
    
    unique_values = []
    duplicate = []
    for item in arr:
        if item not in unique_values:
            unique_values.append(item)
        else:
            duplicate.append(item)
    
    if len(duplicate):
        return "yes duplicate found"
    else:
        return "all are unique values"
           


arr = [1,20,30,44,5,56, 57, 8, 19, 10,31,12, 13, 14, 35, 16, 27, 21]
print(all_unique(arr))