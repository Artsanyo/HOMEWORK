list_1 = [1, "A", 5, "E", 3, "C", 2, "B", 4, "D"] 
index_position = 1
index_value = 144


def replace_index(list_x):
    """Print the index of element with value 144"""
    # blank_list = []
    # blank_list = list_x
    print("The given list is", len(list_1), "indexes long.", "\t\nOriginal list:", list_x)
    copy_of_original_list = list_x
    copy_of_original_list.insert(index_position, index_value) # replace index of 2 with value 144
    print(copy_of_original_list)
    new_list = copy_of_original_list
    print("The index position of value", index_value, "is", new_list.index(144))
  
replace_index(list_1)