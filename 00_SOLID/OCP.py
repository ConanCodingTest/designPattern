#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# SOLID：Open Close Principle(開放封閉原則)

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

if __name__ == "__main__":
    zoo = Zoo()
    zoo.addAnimal(TerrestrialAnimal("Dog"))
    zoo.addAnimal(AquaticAnimal("Fish"))
    zoo.addAnimal(BirdAnimal("Bird"))
    zoo.displayActivity()
    # 增加一個種類(鳥類)只需要增加Animal的子類別，其他程式不更動