#Пингвины не летают - пример неверного использования программирования

# class Bird: # Bird class
#     def __init__(self, name):
#         self.name = name
#
#     def fly(self):
#         print(f"{self.name} летает")
#
#
# class Ping(Bird): # Bird class
#     pass
#
# p = Ping("Cара") # создание объекта класса Ping из класса Bird присваиваем ему имя Cара
#
# p.fly() #вызываем функцию fly из класса Ping

# использование LSP, Liskov substitution Principle для программирования пингвинов которые не летают

class Bird: # птица
     def fly(self):
         print("Эта птица летает")

class Duck(): # леающая птица
    def fly(self):
        print("Эта утка летает быстро")

def fly_in_the_sky(animal): # функция fly_in_the_sky принимает объект класса Bird или Duck
    animal.fly()

# создаем объект класса Bird и класса Duck и вызываем функцию fly_in_the_sky

bird = Bird()
duck = Duck()
fly_in_the_sky(bird)
fly_in_the_sky(duck)