unsorted_list = [1, 2, 3, 8, 9, 10, 5, 7, 6, 4]
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def checkif_reverselist(list_1):
    """Scrieti o functie care returneaza True daca lista primita ca param. este sortata,
    altfel returneaza False."""
    # list_1 = [1, 2, 3, 8, 9, 10, 5, 7, 6, 4]
    list_2 = list_1.copy()
    list_3 = list_2.sort()
    if list_1 != list_2:
        return False
    else:
        return True

print(checkif_reverselist(sorted_list), sorted_list)
