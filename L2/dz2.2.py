number = int(input("Введите число: "))

x1, number = divmod(number, 10000)
x2, number = divmod(number, 1000)
x3, number = divmod(number, 100)
x4, number = divmod(number, 10)
x5, number = divmod(number, 1)

reversed_number = x1 * 1 + x2 * 10 + x3 * 100 + x4 * 1000 + x5 * 10000

print(reversed_number)
