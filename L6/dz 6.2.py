seconds = int(input("Введіть кількість секунд: "))

days, remainder = divmod(seconds, 86400)  # 1 день = 86400 секунд
hours, remainder = divmod(remainder, 3600)  # 1 година = 3600 секунд
minutes, seconds = divmod(remainder, 60)  # 1 хвилина = 60 секунд

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
    day_word = "дні"
else:
    day_word = "днів"

hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)

print(f"{days} {day_word}, {hours_str}:{minutes_str}:{seconds_str}")