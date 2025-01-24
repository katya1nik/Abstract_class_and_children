"""
## Задание 👷‍♂️

Создайте модуль `file_classes.py`, содержащий следующие классы:

Родитель: `ABC`
   - М### Абстрактный класс и его наследники

1. **Класс `AbstractFile`**
   - Методы:
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

from abc import ABC, abstractmethod
import json
import csv

class AbstractFile(ABC):
    """
    Абстрактный класс для выполнения операций с файлами.
    """
    @abstractmethod
    def read(self):
        """
        Абстрактный метод для чтения.
        """
        pass

    @abstractmethod
    def write(self, data):
        """
        Абстрактный метод для записи.
        """
        pass

    @abstractmethod
    def append(self, data):
        """
        Абстрактный метод для дозаписи данных.
        """
        pass

class JsonFile(AbstractFile):
    """
    Класс для работы с JSON-файлами.
    """
    def __init__(self, file_path: str):
        """
        Инициализация объекта Json.
        """
        self.file_path = file_path

    def read(self):
        """
        Чтение данных из JSON-файла.
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write(self, data):
        """
        Запись данных в JSON-файл.
        """
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def append(self, data):
        """
        Дозапись данных в JSON-файл.
        """
        try:
            new_data = self.read()
            if isinstance(new_data, list):
                new_data.append(data)
            else:
                new_data = [new_data, data]
            self.write(new_data)
        except FileNotFoundError:
            self.write([data])

            

