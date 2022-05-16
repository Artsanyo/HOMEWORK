import random


randomlist_numbers = []
for i in range(0,4):
    x = random.randint(1,100)
    randomlist_numbers.append(x)
print(randomlist_numbers)


randomlist_alpha_uppercase = []
for i in range(0,3):
    y = random.randint(65,91)
    randomlist_alpha_uppercase.append(chr(y))
print(randomlist_alpha_uppercase)

randomlist_alpha_lowercase = []
for i in range(0,3):
    y = random.randint(97,123)
    randomlist_alpha_lowercase.append(chr(y))
print(randomlist_alpha_lowercase)

joint_list = randomlist_numbers + randomlist_alpha_lowercase + randomlist_alpha_uppercase

print(joint_list)
