"""
Создайте класс который будет устанавливать свойство name и иметь метод
который к имени прибавляет надпись "гений". Создайте еще 1 класс, унаследуйте предыдущий.
Во втором классе вызовите метод класса родителя и добавьте к выводу надпись "но его отчислят если он не будет учить ООП".
Создайте экземпляр второго класса с вашим именем и вызовите метод печатающий всю надпись.
"""

class Genius:

    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f'{self.name} гений')

class NO(Genius):
    def __init__(self, name):
        super().__init__(name)

    def kill(self):
        print(f'{self.name} гений, но его отчислят если он не будет учить ООП')

name, name2 = Genius('Женя'),NO('Тимур')
name.print_info()
name2.kill()
