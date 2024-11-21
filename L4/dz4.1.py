numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
non_zero_elements = [x for x in numbers if x != 0]
zero_count = numbers.count(0)
numbers = non_zero_elements + [0] * zero_count
print(numbers)