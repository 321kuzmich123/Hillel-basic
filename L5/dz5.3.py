import string


text = input('Type text:')
text = text.title().replace(' ', '')
for i in string.punctuation:
    text = text.replace(i, '')
text = f'#{text}'[:140]
print(text)