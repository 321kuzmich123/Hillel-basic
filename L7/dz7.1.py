def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

name = input("Введіть ваше ім'я: ")
age = int(input("Введіть ваш вік: "))

print(say_hi(name, age))

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')