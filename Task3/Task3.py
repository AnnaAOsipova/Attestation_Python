# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD.

from datetime import datetime, timedelta

def date_from_now(days_from_now):
    today = datetime.now()
    future_timedelta = timedelta(days=days_from_now)
    future_date = today + future_timedelta
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    return formatted_future_date

if __name__ == '__main__':
    days = 9
    date = date_from_now(days)
    print(f'Через {days} дней будет {date}')

