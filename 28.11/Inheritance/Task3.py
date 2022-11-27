"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""

class SpaceObject():
    def __init__(self, size):
        self.size = size

class Star(SpaceObject):
    def __init__(self, size, brightness):
        super().__init__(size)
        self.brightness = brightness
    def shining(self):
        print(f'Яркость звезды: {self.brightness}')

class Planet(SpaceObject):
    def __init__(self, size, population, growth):
        super().__init__(size,)
        self.population = population
        self.growth = growth
    def population_per_year(self, years):
        print(f'Через {years} лет численность населения составит {self.population + self.growth * years}')

star = Star(150,200)
star.shining()

planet = Planet(300, 1000, 100)
planet.population_per_year(2)