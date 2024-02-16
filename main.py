from datetime import datetime
def days_to_birthday(birthday):
    if birthday:
        today = datetime.now().date()
        next_birthday_year = today.year
        birthday_this_year = datetime.strptime(birthday, '%Y-%m-%d').date().replace(year=next_birthday_year)
        if today > birthday_this_year:
            next_birthday_year += 1
            birthday_this_year = birthday_this_year.replace(year=next_birthday_year)
        days_left = (birthday_this_year - today).days
        return days_left
    else:
        return None
# today = datetime.now().date()
# print(today)
# days_left = days_to_birthday('1990-02-17')
# print(days_left)
