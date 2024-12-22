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
