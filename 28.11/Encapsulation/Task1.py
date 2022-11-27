"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""

class Account():
    def __init__(self, name, balance, passport):
        self._name = name
        self.__balance = balance
        self.__passport = passport


    def getbalance(self):
        return self.__balance

    def getpassport(self):
        return self.__passport


    def setbalance(self, newbalance):
        if newbalance < 0:
            print("У вас недостаточно денег")
        else:
            print("Вызывли степпер")
            self.__balance = newbalance


    def setnomerpassport(self,password,passport):
        if password == "1234":
            print("Вы вошли в систему")
            self.__passport = passport
        else:
            print("Измените пароль")


    def delpassport(self, password):
        if password == "1234":
            del self.__passport

account = Account('Женя', 1500, 123768)
print(account.getbalance())
print(account.getpassport())
account.setbalance(100)
account.setnomerpassport(1234,65656)
account.delpassport(1234)