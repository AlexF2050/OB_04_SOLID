#    Условия выполнения задания: Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры,
# программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации
from pprint import PrettyPrinter
from time import monotonic_ns
#    Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия,
# не изменяя существующий код бойцов или механизм боя.
#    Исходные данные:
#    Есть класс Fighter, представляющий бойца.
#    Есть класс Monster, представляющий монстра.
# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
#    Шаг 1: Создайте абстрактный класс для оружия
# Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().
#    Шаг 2: Реализуйте конкретные типы оружия
# Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow. Каждый из этих классов реализует метод attack() своим уникальным способом.
#    Шаг 3: Модифицируйте класс Fighter
# Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
# Добавьте метод change_weapon(), который позволяет изменить оружие бойца.
#    Шаг 4: Реализация боя
# Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
#    Требования к заданию:
# Код должен быть написан на Python.
# Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
# Программа должна выводить результат боя в консоль.
# Пример результата:
# Боец выбирает меч.
# Боец наносит удар мечом.
# Монстр побежден!
# Боец выбирает лук.
# Боец наносит удар из лука.
# Монстр побежден!

#_______________________________________ Создаём классы Fighter, Monster, Weapon________________________________________

# Импортируем библиотеки необходимые для создания игры
import pygame #импортируем библиотеку pygame
pygame.init() #инициализируем pygame

# Создаём класс Fighter, представляющий бойца.
# Шаг 3.1: Модифицируйте класс Fighter
# Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.

class Fighter:
    def __init__(self, weapon):
        self.weapon = weapon

# Шаг 3.2: Добавьте метод change_weapon(), который позволяет изменить оружие бойца.
    def change_weapon(self, weapon):
        self.weapon = weapon

# Создаём класс Monster, представляющий монстра.
class Monster:
    def __init__(self):
        self.is_live = True

    def take_damage(self):
        self.is_live = False

# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
# Шаг 1: Создайте абстрактный класс для оружия
# Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().

from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуйте конкретные типы оружия
# Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow.
# Каждый из этих классов реализует метод attack() своим уникальным способом.
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет в монстра стрелой из лука."

#_______________________________________ Создаём объекты и действия_____________________________________________________

# Используем выше созданные классы и создаём объекты и действия
print(" ")
print(">>> ИГРА НАЧАЛАСЬ >>>")
print(" ")
print("В тёмном лесу, Боец встречает монстра и молниеносно действует:")

def fight(fighter, monster): #функция fight() принимает два аргумента: объекты и действие
    if fighter.weapon.attack() is not None: #проверяем, есть ли оружие у бойца
        print(fighter.weapon.attack()) #выводим результат боя в консоль
        monster.take_damage() #выстреляем в монстра
        if not monster.is_live:
            print("Монстр побежден!")

def main():
    fighter = Fighter(Sword()) #создаём объект класса Fighter
    monster = Monster() #создаём объект класса Monster

    print("Боец выбирает меч.")
    fight(fighter, monster) #вызываем функцию fight()
    print(" ")
    print(">>> Боец идёт по лесу и вдалеке видит другого монстра. Он принимает решение сменить оружие:")


    fighter.change_weapon(Bow()) #создаём объект класса Fighter
    print("\nБоец выбирает лук и стрелы.")
    fight(fighter, monster)  # вызываем функцию fight() с новым оружием

    print(" ")
    print(">>> ИГРА ОКОНЧЕНА ]]]")

if __name__ == "__main__": #проверяем, является ли программа главной
    main() #вызываем функцию main()







