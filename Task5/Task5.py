# Напишите код, который запускается из командной строки и получает на вход путь
# до директории на ПК. Соберите информацию о содержимом в виде объектов
# namedtuple. Каждый объект хранит: имя файла без расширения или название
# каталога, расширение, если это файл, флаг каталога, название родительского
# каталога. В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import os
import logging
from collections import namedtuple
from argparse import ArgumentParser

logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='{asctime} - {levelname} - {message}',
                    style='{', encoding='utf-8')
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def collect_directory_info(directory_path):
    logging.info(f"Запуск функции для директории: {directory_path}")

    if not os.path.isdir(directory_path):
        logging.error(f"Указанный путь не является директорией: {directory_path}")
        return

    logging.info(f"Содержимое директории: {directory_path}")

    try:
        for entry in os.listdir(directory_path):
            full_path = os.path.join(directory_path, entry)
            parent_directory = os.path.basename(directory_path)

            if os.path.isdir(full_path):
                file_info = FileInfo(name=entry, extension='', is_directory=True, parent_directory=parent_directory)
                logging.info(f"Каталог: {file_info}")
                collect_directory_info(full_path)
            else:
                name, extension = os.path.splitext(entry)
                file_info = FileInfo(name=name, extension=extension.lstrip('.'), is_directory=False,
                                     parent_directory=parent_directory)
                logging.info(f"Файл: {file_info}")
    except Exception as e:
        logging.error(f"Ошибка при обработке директории: {e}")


def main():
    parser = ArgumentParser(description="Сбор информации о директории")
    parser.add_argument('directory', type=str, help="Путь до директории")
    args = parser.parse_args()

    directory_path = args.directory
    # path = input("Введите путь до директории: ")  # Вводим путь до директории
    # file_infos = collect_directory_info(directory_path(path).resolve())  # Собираем информацию о содержимом
    # with open("directory_info.log", "w") as file:  # Создаём файл для сохранения данных
    #     file.write(str(file_infos))  # Сохраняем данные в виде строки
    try:
        collect_directory_info(directory_path)
        print(f'Информация о содержимом директории "{directory_path}" успешно записана в файл')
    except ValueError as e:
        print(e)

if __name__ == '__main__':

    main()
