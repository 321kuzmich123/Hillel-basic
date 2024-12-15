a = int(input("Enter number "))
operator = input( "введите знак операции( +, -, *, /)")
b = int(input("Enter number "))
if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    if b != 0:
        result = a / b
    else:
        result = " ошибка: деление на ноль "
print( result )
continue_calculating = input("продолжить? (y/n): ").lower()
if continue_calculating not in ['y', 'yes']:
    print("Calculator is exiting.")