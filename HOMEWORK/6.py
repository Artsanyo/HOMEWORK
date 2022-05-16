list_1 = [1, "A", 5, "E", 3, "C", 2, "B", 4, "D"] 
def replace_index(list_x):
    """Replace second element with 144"""
    blank_list = []
    blank_list = list_x
    print("The given list is", len(list_1), "indexes long.", "\t\nOriginal list:", list_x)
    copy_of_original_list = list_x.copy()
    copy_of_original_list.insert(1, 144) # replace index of 2 with value 144
    print("New list    : ", copy_of_original_list)
    


replace_index(list_1)
