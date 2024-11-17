my_list = [1, 2, 3, 1, 5]
if my_list:
    mid = (len(my_list)+1) // 2
    list1 = my_list[:mid]
    list2 = my_list[mid:]
else:
    list1 = []
    list2 = []
print(list1, list2)