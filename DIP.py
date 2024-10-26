# # Принцип инверсии зависимости (DIP, Dependency Inversion Principle)
# class Book:
#     def read(self):
#         print("история книги")
#
# # Создание класса, чтобы связать классы Book и Publisher
#
# class StoryReader:
#     def __init__(self):
#         self.book = Book()
#
#     def tell_story(self):
#         print(self.book)

from abc import ABC, abstractmethod # Импорт библиотеки ABC из модуля ab

class StorySource(ABC): # Импорт библиотеки ABC из модуля ab
    @abstractmethod # Импорт библиотеки ABC из модуля ab
    def get_story(self): # Переопределяем метод get_story
        pass

class Book(StorySource):
    def get_story(self): # Переопределяем метод get_story
        print("Чтение интересной книги")

class audioBook(StorySource):
    def get_story(self): # Переопределяем метод get_story
        print("Слушаем аудиокнигу")

class StoryReader():
    def __init__(self, story_source: StorySource): # Переопределяем конструктор класса StoryReader с параметром story_source
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story() # Переопределяем метод get_story из класса StorySource в классе StoryReader

# создаем объект классов

book = Book()
audioBook = audioBook()

readerBook = StoryReader(book)
readerAudioBook = StoryReader(audioBook)

readerBook.tell_story() # Переопределяем метод tell_story из класса StoryReader в классе StoryReader класса Book
readerAudioBook.tell_story() # Переопределяем метод tell_story из класса StoryReader в классе StoryReader класса audioBook




