# Принцип открытости-закрытости (OCP) в программировании
# (Open-Closed Principle)

 # Определение
 # Принцип открытости-закрытости (OCP) в программировании
 # предполагает, что программные сущности должны быть открыты для расширения,
 # но закрыты для модификации. Это означает, что сущности могут быть изменены
 # путем добавления новых функциональных возможностей, но не путем изменения
 # существующего кода.

 # Пример
 # В данном примере мы рассмотрим класс Car, который представляет собой автомобиль.
 # Класс Car имеет метод drive(), который позволяет автомобилю двигаться вперед.
 # Мы можем расширить класс Car, добавив новый метод, например, turn(), который
 # позволяет автомобилю поворачивать влево или вправо. Это соответствует принципу
 # открытости-закрытости, поскольку мы можем добавлять новые функциональные возможности
 # без изменения существующего кода.

 # Применение
 # Принцип открытости-закрытости можно применять в различных областях программирования.
 # Например, при создании библиотек или фреймворков, где необходимо обеспечить
 # возможность расширения существующих классов или функций без изменения их кода.

# модуль для работы с абстрактными классами

from abc import ABC, abstractmethod # абстрактный класс ABC импортируем из модуля abc

class Formated(ABC): # абстрактный класс Formated
    @abstractmethod # абстрактный метод abstractmethod импортируем из модуля abc
    def format(self, report): # абстрактный метод format импортируем из модуля abc и переопределяем в классе Formated
        pass

class TextFormated(Formated): # класс TextFormated наследуем от абстрактного класса Formated
    def format(self, report): # переопределяем в классе TextFormated метод format
        print(report.title) # выводим заголовок
        print( report.content) # выводим контент

class HtmlFormated(Formated): # класс TextFormated наследуем от абстрактного класса Formated
    def format(self, report): # переопределяем в классе TextFormated метод format
        print(f"<h>{report.title}</h>") # выводим заголовок
        print(f"<h>{report.content}</h>")  # выводим контент

class Report(): # класс Report наследуем от абстрактного класса Formated
    def __init__(self, title, content, formated): # переопределяем в классе Report метод __init__ и переопределяем в абстрактном классе Formated
        self.title = title
        self.content = content
        self.formated = formated

    def docPrinter(self): # переопределяем в классе Report метод docPrint
        self.formated.format(self) # вызываем метод format класса Formated


report = Report('Заголовок отчета', 'текст отчёта его тут много', HtmlFormated())

report.docPrinter()
