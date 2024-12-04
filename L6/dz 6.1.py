import string

def get_letters_between(input_str):
    all_letters = string.ascii_letters
    start, end = input_str.split('-')
    start_idx = all_letters.index(start)
    end_idx = all_letters.index(end)
    return all_letters[start_idx:end_idx + 1]
print(get_letters_between("s-A"))