number = int(input(" четырёхзначное число: "))

thousands, remainder = divmod(number, 1000)
hundreds, remainder = divmod(remainder, 100)
tens, ones = divmod(remainder, 10)

print(thousands)
print(hundreds)
print(tens)
print(ones)