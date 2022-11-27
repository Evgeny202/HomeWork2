"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""
import time

class Hero():
    def __init__(self,health, power):
        self.health = health
        self.power = power

class Magician(Hero):
    def __init__(self,health, power):
        super().__init__(health, power)

    def hello(self):
        print('Ну здорова')

    def atack(self, persona):
        persona.health -= self.power * 2
        self.power -= 2
        print('попал')

hero = Hero(121, 15)
mag = Magician(121, 15)
mag.hello()
mag.atack(hero)
print(f'магическая сила: {mag.power}')
print(f'здоровье героя: {hero.health}')