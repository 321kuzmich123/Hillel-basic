def add_one(some_list):
    string_number = ""
    for digit in some_list:
        string_number += str(digit)
    number = int(string_number)
    number += 1
    new_string_number = str(number)
    new_list = []
    for char in new_string_number:
        new_list.append(int(char))
    return new_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")