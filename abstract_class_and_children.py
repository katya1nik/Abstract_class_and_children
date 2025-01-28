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
        with open(self.file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')

                
    def append(self, *lines: str) -> None:
        """
        Метод для добавления данных в текстовый файл.
        """
        with open(self.file_path, 'a', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')
        

class JsonFile(AbstractFile):
    """
    Класс для работы с JSON-файлами.
    """
    def read(self) -> list[dict]:
        """
        Метод для чтения данных из JSON-файла.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Файл {self.file_path} не найден") from e

        except json.JSONDecodeError as e:
            raise ValueError(f"Файл{self.file_path} вероятно не найден") from e
        

    def write(self, *data: dict) -> None:
        """
        Метод для записи данных в JSON-файл.
        """
        # data_list_dicts = [json.dumps(data) for data in data]
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Файл {self.file_path} не найден") from e

    def append(self, *data: dict) -> None:
        """
        Метод для добавления данных в JSON-файл.
        """
        old_data = self.read()
        old_data.extend(data)
        self.write(*old_data)

class CsvFile(AbstractFile):
    """
    Класс для работы с CSV-файлами.
    """
    def read(self) -> list[dict]:
        """
        Метод для чтения данных из CSV-файла.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                return list(reader)
            
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Файл {self.file_path} не найден") from e
        
        except Exception as e:
            raise e
        
    def write(self, *data: dict) -> None:
        """
        Метод для записи данных в CSV-файл.
        """
        try:
            with open(self.file_path, 'w', encoding='utf-8-sig', newline='') as file: 
                writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=',')
                writer.writeheader()
                writer.writerows(data)

        except PermissionError as e:
            raise PermissionError(f"Файл {self.file_path} занят другим процессом") from e
        
    def append (self, *data: dict) -> None:
        """
        Метод для добавления данных в CSV-файл.
        """
        try:
            with open(self.file_path, 'a', encoding='utf-8-sig', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writerows(data)

        except PermissionError as e:
            raise PermissionError(f"Файл {self.file_path} занят другим процессом") from e
        
if __name__ == "__main__":
    txt_file = TxtFile('data.txt')
    txt_file.write('Hello, world!', 'This is a test.')
    txt_file.append('This is another line.')
    print(txt_file.read())

json_file = JsonFile('data.json')

data = [
  {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "Alice",
        "age": 25,
        "city": "London"
    },
] 

json_file.write(*data)

new_data = [
    {
        "name": "Bob",
        "age": 35,
        "city": "Paris"
    },
    {
        "name": "Emily",
        "age": 28,
        "city": "Berlin"
    }
]
json_file.append(*new_data)
print(json_file.read())

csv_file = CsvFile('data.csv')

csv_file.write(*data)
csv_file.append(*new_data)
print(csv_file.read())