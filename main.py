from datetime import datetime


def days_to_birthday(birthday):
    # Перевірка чи введено дату народження
    if birthday:
        # Отримання поточної дати
        today = datetime.now().date()

        # Визначення року наступного дня народження
        next_birthday_year = today.year

        # Перетворення рядка з датою народження у об'єкт datetime.date
        # заміна року на поточний та перевірка на коректність коду
        try:
            birthday_this_year = datetime.strptime(birthday, '%Y-%m-%d').date().replace(year=next_birthday_year)
        except:
            print('Date of birth entered incorrectly')
            return None
        # Якщо день народження вже пройшов у поточному році, перенесення його на наступний рік
        if today > birthday_this_year:
            next_birthday_year += 1
            birthday_this_year = birthday_this_year.replace(year=next_birthday_year)

        # Обчислення кількості днів до наступного дня народження
        days_left = (birthday_this_year - today).days

        return days_left
    else:
        # Повернення значення None, якщо дата народження не була введена
        return None

# Приклад використання функції
# today = datetime.now().date()
# print(today)
# days_left = days_to_birthday('1990-02-17')
# print(days_left)
# days_left = days_to_birthday('1231241')
# print(days_left)
