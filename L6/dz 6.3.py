def multiply_digits_until_single(num):
    while num > 9:
        product = 1
        while num > 0:
            digit = num % 10
            product *= digit
            num //= 10
        num = product
    return num

number = int(input("Введіть ціле число: "))
print(f"Результат: {multiply_digits_until_single(number)}")