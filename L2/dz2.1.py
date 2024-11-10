number = int(input(" четырёхзначное число: "))

a, b = divmod(number, 1000)
c, b = divmod(b, 100)
x, y = divmod(b, 10)

print(a)
print(c)
print(x)
print(y)