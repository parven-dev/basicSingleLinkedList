

my_tuples = ("a", "b", "c", "d")
searching_value = "c"
def searching_element(tuples: tuple, ele):
    for item in range(len(tuples)):
        if tuples[item] == ele:
            return tuples.index(tuples[item])



print(searching_element(my_tuples, searching_value))
