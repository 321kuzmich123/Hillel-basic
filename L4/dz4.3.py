import random
my_list = [random.randint(1,9) for i in range(random.randint(3, 10))]
new_list = [my_list[0], my_list[2], my_list[-2]] if len(my_list) > 2 else my_list
print(my_list)
print(new_list)

