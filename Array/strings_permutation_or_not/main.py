
def string_permutation(list1:list, list2:list):
    
    check_list = []
    if len(list1) == len(list2):
        for string in list1:
            if string in list2 not in check_list:
                check_list.append(string)
    
    if len(check_list) != len(list1) and len(list2):
        return "its not permuation string"
    
    elif type(list1) == int or type(list2) == str:
        return "its not pemuation"
    else:
        return "its permuation string"
    
            


list1  = ["s", "i", "l", "e","n", "t"]
list2 =  ["l", "i", "s", "t", 'e', "n"]

print(string_permutation(list1, list2))


