list_1 = [1, 2, 3, 8]
list_2 = [5, 6, 7, 6]


def multiplylist_indices (list_1, list_2):
    empty_list = []
    for elements in range(0, len(list_1)):
        empty_list.append(list_1[elements] * list_2[elements])
    return empty_list


print(multiplylist_indices(list_1, list_2))