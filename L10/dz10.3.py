def is_even(digit):
    return digit % 2 == 0

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
assert is_even(8) == True, 'Test4'  # Тест для числа 8
print('OK')