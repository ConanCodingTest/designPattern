#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# SOLID：Liskov Substitution Principle(里氏替換原則)

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定義抽象類別和抽象方法

class Animal(metaclass=ABCMeta):
    """動物"""

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def moving(self):
        pass

class TerrestrialAnimal(Animal):
    """陸生生物"""

    def __init__(self, name):
        super().__init__(name)

    def moving(self):
        print(self._name + "在地上跑...")


class AquaticAnimal(Animal):
    """水生動物"""

    def __init__(self, name):
        super().__init__(name)

    def moving(self):
        print(self._name + "在水中游...")


class BirdAnimal(Animal):
    """鳥類動物"""

    def __init__(self, name):
        super().__init__(name)

    def moving(self):
        print(self._name + "在天空飛翔...")

class Monkey(TerrestrialAnimal):
    """猴子"""

    def __init__(self, name):
        super().__init__(name)

    def climbing(self):
        print(self._name + "在爬樹，動作靈活輕盈...")


# 修改Zoo類別，增加climbing方法：
class Zoo:
    """動物園"""

    def __init__(self):
        self.__animals =[]

    def addAnimal(self, animal):
        self.__animals.append(animal)

    def displayActivity(self):
        print("觀察每一種動物的活動方式：")
        for animal in self.__animals:
            animal.moving()

    def monkeyClimbing(self, monkey):
        monkey.climbing()

if __name__ == "__main__":
    zoo = Zoo()
    zoo.addAnimal(TerrestrialAnimal("Dog"))
    zoo.addAnimal(AquaticAnimal("Fish"))
    zoo.addAnimal(BirdAnimal("Bird"))
    monkey = Monkey("Monkey")
    zoo.addAnimal(monkey)
    zoo.displayActivity()
    print()
    print("觀察猴子的爬樹行為：")
    zoo.monkeyClimbing(monkey)
    #Zoo的addAnimal方法接受Animal類別的物件，所以Animal的子類別可以傳入 
    #但Zoo的monkeyClimbing只接受Monkey類別物件