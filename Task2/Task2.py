# Напишите скрипт, который получает текущее время и дату , а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году.

import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='{asctime} - {msg}', style='{')

def current_datetime():
    now = datetime.now()
    formatted_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
    day_of_week = now.strftime('%A')
    week_number = now.isocalendar()[1]

    logging.info(f'Текущая дата и время: {formatted_datetime}')
    logging.info(f'День недели: {day_of_week}')
    logging.info(f'Номер недели: {week_number}')

if __name__ == '__main__':
    current_datetime()