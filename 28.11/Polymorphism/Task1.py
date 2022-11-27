"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""
class People():
    def quack(self):
        print("Я имитирую кряканье")


    def clothes(self):
        print("На мне одежда")


class Duck(People):
    def quack(self):
        print("Я крякаю")


    def clothes(self):
        print("На мне перья")

a = People()
b = Duck()
ab = [a, b]
for i in ab:
    i.quack()
    i.clothes()

