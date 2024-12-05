import string

input_str = input("Введіть літери у форматі 'літера1-літера2': ")
all_letters = string.ascii_letters
start, end = input_str.split('-')
start_idx = all_letters.index(start)
end_idx = all_letters.index(end)
if start_idx <= end_idx:
    result = all_letters[start_idx:end_idx + 1]
else:
    result = all_letters[start_idx:] + all_letters[:end_idx + 1]
print(result)
