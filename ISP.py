# # Принцип разделения интерфейсов (ISP, Interface Segregation Principle)
#
# создадим отдельные классы для каждого интерфейса

class Light():
    def turn_on(self):
        print(f"Light is on")

class Food():
    def eat(self):
        print(f"Food is eating")


class Music():
    def turn_on(self):
        print(f"Music is on")

# Создадим объекты для каждого интерфейса
light = Light()
food = Food()
music = Music()

# вызов функции для каждого интерфейса
light.turn_on()
food.eat()
music.turn_on()
