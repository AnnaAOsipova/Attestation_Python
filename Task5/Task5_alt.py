import os
from collections import namedtuple
from pathlib import Path

def get_file_info(path):
    """
    Функция для сбора информации о содержимом директории.
    """
    file_info = []
    for item in os.listdir(path):  # Перебираем все элементы в директории
        item_path = Path(os.path.join(path, item))  # Получаем полный путь к элементу
        if item_path.is_dir():  # Если элемент является каталогом
            file_info.append(FileItem(item, None, True, os.path.dirname(item_path)))  # Добавляем объект FileItem с информацией о каталоге
        else:  # Если элемент не каталог
            file_info.append(FileItem(item.split(".")[0], item.split(".")[-1], False, os.path.dirname(item_path)))  # Добавляем объект FileItem с информацией о файле
    return file_info

class FileItem(namedtuple('FileItem', ['name', 'extension', 'is_directory', 'parent'])):
    pass

def main():
    path = input("Введите путь до директории: ")  # Вводим путь до директории
    file_infos = get_file_info(Path(path).resolve())  # Собираем информацию о содержимом
    with open("directory_info_alt.log", "w") as file:  # Создаём файл для сохранения данных
        file.write(str(file_infos))  # Сохраняем данные в виде строки

if __name__ == "__main__":
    main()
