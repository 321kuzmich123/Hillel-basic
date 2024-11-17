my_list = [1, 2, 3, 4, 5]
if my_list:
    last_element = my_list.pop()
    my_list.insert(0,last_element)
print( my_list )