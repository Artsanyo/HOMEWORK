original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def reverse_alist (list_x):
    """Scrieti o functie care returneaza reversul unei liste. Lista primita ca parametru nu 
    trebuie modificata."""
    list_x = list(list_x)  #took the parameter from the function to create a new list
    list_y = list_x.copy() # New list y == a copy of list x
    list_y.reverse()       #reverse list_y
    return list_y


print("\tOriginal list:", original_list, "\n\tReversed list:", reverse_alist(original_list)) #asign original_list as a parameter to reverse_alist function/call the function