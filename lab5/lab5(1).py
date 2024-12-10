class Book:  # определение класса book 
    def __init__(self, title, author, year):  # инициализация объекта класса book
        self.title = title  # присвоение атрибута 
        self.author = author  # присвоение атрибута 
        self.year = year  # присвоение атрибута 
    def get_info(self):  # метод для получения информации о книге
        return f"Название книги: {self.title}, Автор: {self.author}, Год: {self.year}"  # возвращение форматированной строки с информацией о книге
title = input("Введите название книги: ")  # ввод 
author = input("Введите автора: ")  # ввод 
year = int(input("Введите год издания: "))  # ввод 
a = Book(title, author, year)  # создание объекта класса book с заданными параметрами
print(a.get_info())  # вывод информации о книге с помощью get_info()