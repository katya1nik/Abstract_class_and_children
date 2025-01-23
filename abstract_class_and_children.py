"""
## Задание 👷‍♂️

Создайте модуль `file_classes.py`, содержащий следующие классы:

Родитель: `ABC`
   - М### Абстрактный класс и его наследники

1. **Класс `AbstractFile`**
   - етоды:
     - `read()`: Абстрактный метод для чтения данных из файла.
     - `write(data)`: Абстрактный метод для записи данных в файл.
     - `append(data)`: Абстрактный метод для добавления данных в файл.

2. **Класс `JsonFile`**
   - Родитель: `AbstractFile`
   - Атрибуты:
     - `file_path`: Путь к файлу.
   - Методы:
     - Реализовать методы `read`, `write` и `append` для работы с JSON-файлами.

3. **Класс `TxtFile`**
   - Родитель: `AbstractFile`
   - Атрибуты:
     - `file_path`: Путь к файлу.
   - Методы:
     - Реализовать методы `read`, `write` и `append` для работы с текстовыми файлами.

4. **Класс `CsvFile`**
   - Родитель: `AbstractFile`
   - Атрибуты:
     - `file_path`: Путь к файлу.
   - Методы:
     - Реализовать методы `read`, `write` и `append` для работы с CSV-файлами.

### Вызов методов

Создайте модуль `file_tests.py`, в котором вы протестируете все созданные классы. Вызовите методы `read`, `write` и `append` для каждого типа файла с использованием конструкции `if __name__ == "__main__":`.
"""

# 1. Работа с файлами JSON
import json


json_string = """
[
    "Иванов Иван Иванович",
    "Петров Петр Петрович"
]
"""

python_data = json.loads(json_string)
print(python_data)

json_string = json.dumps(python_data, ensure_ascii=False, indent=4)
print(json_string)


 #  Создание функции для записи в файл json
def write_json(*data: str, file_path: str, encoding: str = "utf-8") -> None:
    """
    Функция записи в json файл.
    :param data: данные для записи
    :param file_path: путь к файлу (в данном случ
ае название файла)
    :param encoding: кодировка
    """
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

name1="Никулина Екатерина Александровна"
name2="Иванов Иван Иванович"

write_json(name1, name2, file_path='name.json')

# Создание функции для чтения json

def read_json(file_path: str, encoding: str = "utf-8") -> list[str]:
    """
    Функция чтения json файла.
    :param file_path: путь к файлу (в данном случае название файла)
    :param encoding: кодировка
    """
    with open(file_path, 'r', encoding=encoding) as file:
        return json.load(file)
    
result = read_json("name.json")
print(result)


# Создание функции для дозаписи в файл JSON:

def append_json(file_path: str, *data: str, indent: int = 4, encoding: str = 'utf-8') -> None:
    """
    Функция дозаписи в json файл.
    :param file_path: путь к файлу (в данном случае название файла)
    :param data: данные для записи
    :param indent: отступ
    :param encoding: кодировка
    """
    with open(file_path, 'r', encoding=encoding) as file:
        python_data = json.load(file)


 # Проверка типа данных
    if not isinstance(python_data, list):
        raise TypeError("Поддерживается только добавление в JSON-массив")

    python_data.extend(data)

    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(python_data, file, ensure_ascii=False, indent=indent)

file = 'name.json'
append_json(file, 'Новое имя 25', 'Новое имя 26', indent=2)

# 2. Работа с файлами CSV
import csv

# Создание функции для записи в файл CSV

name_list = [

    ["Иванов", "Иван", "Иванович"],
    ["Петров", "Петр", "Петрович"],
]

def write_csv(data, file_path, delimiter=';', encoding: str ='utf-8-sig') -> None:
    """
    Функция записи в csv файл.
    :param data: данные для записи
    :param file_path: путь к файлу (в данном случае название файла)
    :param delimiter: разделитель
    :param encoding: кодировка
    """
    with open(file_path, 'w', encoding=encoding) as file:
        writer = csv.writer(file, delimiter=delimiter, lineterminator="\n")
        writer.writerows(name_list)
write_csv(name_list, file_path='name.csv')


# Создание функции для чтения CSV
def read_csv(file_path, delimiter=';', encoding: str ='utf-8-sig')-> list[str]:
    """
    Функция чтения csv файла.
    :param file_path: путь к файлу (в данном случае название файла)
    :param delimiter: разделитель
    :param encoding: кодировка
    """
    with open(file_path, 'r', encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter)
        return list(reader)
name_list = read_csv("name.csv")


# Создание функции для дозаписи в файл CSV
new_name = ["Иванова", "Мария", "Петровна"]
def append_csv(file_path, data, delimiter=';', encoding: str ='utf-8-sig') -> None:
    """
    Функция дозаписи в csv файл.
    :param file_path: путь к файлу (в данном случае название файла)
    :param data: данные для записи
    :param delimiter: разделитель
    :param encoding: кодировка
    """
    with open(file_path, 'a', encoding=encoding) as file:
        writer = csv.writer(file, delimiter=delimiter, lineterminator="\n")
        writer.writerow(data)
append_csv("name.csv", new_name)
result = read_csv("name.csv")
print(result)


# Работа с файлами TXT

txt_file = "name.txt"

# Функция для записи в файл TXT
def write_txt(*data: str, file_path, mode: str = "w", encoding: str = "utf-8") -> None:
    """
    Функция записи в txt файл.
    :param data: данные для записи
    :param file: файл для записи
"""
    
    with open(file_path, mode, encoding=encoding) as file:
        for line in data:
            file.write(line + "\n")


data = ["В лесу родилась елочка,", "В лесу она росла,",]

write_txt(*data, file_path="name.txt")
print("name.txt",*data)

# # Функция дозаписи в файл TXT
def append_txt(*data: str, file_path, mode: str = "a", encoding: str = "utf-8") -> None:
    """
    Функция дозаписи в txt файл.
    :param data: данные для записи
    :param file: файл для записи
"""
    with open(file_path, mode, encoding=encoding) as file:
        for line in data:
            file.write(line + "\n")

data = ["Зимой и летом стройная,", "Зеленая была."]
append_txt(*data, file_path="name.txt")
print("name.txt",*data)

# Функция чтения из файла TXT
def read_txt(file_path, encoding: str = "utf-8") -> list[str]:
    """
    Функция чтения из txt файла.
    """
    with open(file_path, encoding=encoding) as file:
        return [line.strip() for line in file.readlines()]

result = read_txt("name.txt")
print(result)

# Работа с файлами YAML
import yaml

config = {
    'app_name': 'Погодное приложение',
    'version': '1.0',
    'admin': 'Екатерина Никулина',
    'settings': {
        'theme': 'light',
        'language': 'ru',
        'notifications': True
    },
    'users': [
        'admin',
        'moderator',
        'guest'
    ]
}


with open('weather_config.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(config, file, default_flow_style=False, allow_unicode=True)

# Функция чтения из YAML
def read_yaml(file_path: str):
    """
    Функция чтения YAML файла
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)
    
data = read_yaml('weather_config.yaml')
print(data)