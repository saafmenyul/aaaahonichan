from datetime import datetime
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Book(Printable):
    category = "General"
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
    

    def info(self):
        return f"Книга называется - {self.title}, её автор - {self.author}, издана она была в {self.year}"


    def __str__(self):
        return self.info()
    

    def print_info(self):
        print(self.info())

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title


    @classmethod
    def from_string(cls, data):
        title, author, year = data.split('/')
        return cls(title, author, int(year))


    @property
    def age(self):
        return datetime.now().year - self.year
    

    @age.setter
    def age(self, value):
        self.year = datetime.now().year - value


class Ebook(Book):
    def __init__(self, title: str, author: str, year: int, format: str):
        super().__init__(title, author, year)
        self.format = format
    

    def info(self):
        return f"Книга называется - {self.title}, её автор - {self.author}, издана она была в {self.year}, формат - {self.format}"





test = Book('Название','Автор', 1902)
print(test.age)
book1 = Book("Название", "Автор", 1111)
print(book1.info())
book2 = Book.from_string('Название/Автор/1111')
print(book2.info())
print(book1 == book2)
book1 = Book("Название", "Автор", 1111)
book1.print_info()
book2 = Book.from_string('Название/Автор/1111')
book2.print_info()