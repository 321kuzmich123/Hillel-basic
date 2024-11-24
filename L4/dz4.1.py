numbers = [1, 0, 13, 0, 0, 0, 5]
non_zero_elements = [x for x in numbers if x != 0]
zero_count = numbers.count(0)
numbers = non_zero_elements + [0] * zero_count
print(numbers)