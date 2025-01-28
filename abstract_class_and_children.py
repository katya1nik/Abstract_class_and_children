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
    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def read(self):
        """
        Абстрактный метод для чтения данных из файла.
        """
        pass

    @abstractmethod
    def write(self):
        """
        Абстрактный метод для записи данных в файл.
        """
        pass

    @abstractmethod
    def append(self):
        """
        Абстрактный метод для добавления данных в файл.
        """
        pass


class TxtFile(AbstractFile):
    """
    Класс для работы с текстовыми файлами.
    """

    def read(self) -> list[str]:
        """
        Метод для чтения данных из текстового файла.
        """
        try:
          with open(self.file_path, 'r', encoding='utf-8') as file:
              return file.readlines()
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Файл {self.file_path} не найден") from e

    def write(self, *lines: str) -> None:
        """"
        Метод для записи данных в текстовый файл.
        """
        try:
          with open(self.file_path, 'w', encoding='utf-8') as file:
              for line in lines:
                  file.write(line + '\n')

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Файл {self.file_path} не найден") from e
                
    def append(self, *lines: str) -> None:
        """
        Метод для добавления данных в текстовый файл.
        """
        try:
          with open(self.file_path, 'a', encoding='utf-8') as file:
              for line in lines:
                  file.write(line + '\n')
        
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Файл {self.file_path} не найден") from e

