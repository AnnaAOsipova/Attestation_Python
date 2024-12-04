# Напишите скрипт , который принимает два аргумента командной строки: число и
# строку . Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе.

import argparse

def Parser():
    parser = argparse.ArgumentParser(description="Обработка числа и строки")
    parser.add_argument('num', type=int, help='Число для вывода')
    parser.add_argument('string', type=str, help='Строка для вывода')
    parser.add_argument('--verbose', action ='store_true', help='Вывод дополнительной информации о процессе')
    parser.add_argument('--repeat', type=int, default=1, help='Количество повторов строки в выводе')
    args = parser.parse_args()

    if args.verbose:
        print(f'Обрабатываем число {args.number} и текст: "{args.text}"')

    for _ in range(args.repeat):
        print(args.text)

if __name__ == '__main__':
    Parser()

