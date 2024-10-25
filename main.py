# # создаём класс, который имеет два способа создания объекта
# class UserManager(): # создаем класс
#     def __init__(self, user): # создаем конструктор класса UserManager с параметром user
#         self.user = user # создаем переменную self.user в классе UserManager с параметром user
#
#     def change_user_name(self, user_name): # создаем метод change_user_name
#         self.user.name = user_name # создаем переменную self.user в классе UserManager с параметром user_name
#
#     def save_user(self): # создаем метод save_user для сохранения данных в базу данных файла users.txt
#         file = open("users.txt", "a") # создаем переменную file в классе UserManager с параметром users.txt и открываем файл
#         file.write(self.user) # создаем переменную file в классе UserManager с параметром self.user и записываем в файл
#         file.close() # закрываем файл

# принцип единственной ответственности
# создадим класс для создания пользователей
class User():# создаем класс
    def __init__(self, user): # создаем конструктор класса User с параметрами user
        self.user = user # создаем переменную self.user в классе User с параметром user

# создадим класс для изменения имени пользователя
class UserNameChanger(): # создаем класс
    def __init__(self, user): # создаем конструктор класса UserNameChanger с параметром user

# создадим метод для изменения имени пользователя
def change_name(self, new_name): # создаем метод change_user_name
        self.user.name = new_name # создаем переменную self.user в классе UserNameChanger с параметром user_name

class SaveUser(): # создаем класс
    def __init__(self, user):  # создаем конструктор класса User с параметрами user
        self.user = user  # создаем переменную self.user в классе User с параметром user

    def save(self): # создаем метод save для сохранения данных в базу данных файла users.txt
        file = open("users.txt", "a") # создаем переменную file в классе UserManager с параметром users.txt и открываем файл
        file.write(self.user) # создаем переменную file в классе UserManager с параметром self.user и записываем в файл
        file.close() # закрываем файл
