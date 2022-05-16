"""Make a function for printing the first 5 longest strings in a list ; (len("test"))"""

x = ["Python is an easy to learn powerful programming language"]

def convert_list(list_x):
    return(list_x[0].split())


def longest_string(list_y):
    count = 0
    for i in list_y:
        if len(i) > count:
            count = len(i)
            word = i
    return word 

print(longest_string(convert_list(x)))




print(convert_list(x))


