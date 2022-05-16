original_list = [1, 12, 344, 33, 534, 96, 117, 58, 10000, 339, 10000]

def print_star_strings():
    print("*" * 100)

def remove_max_value(list_x):
    """Make a function to remove all the element with a maximal value from a list; 
    return a new list (original list does not modify)"""
    new_list = list_x.copy()
    print_star_strings()
    # print("Original list before sorting:  ", new_list)
    original_list_sorted = new_list.copy()
    original_list_sorted.sort()
    print("Original list after sorting:   ",original_list_sorted)
    original_list_sorted.pop() # original list is sorted
    print_star_strings()
    print("Original list sorted \nafter sorting, max was removed:",original_list_sorted)
    print_star_strings()
    return new_list
    
print("Original list before sorting:  ", remove_max_value(original_list))
print_star_strings()
