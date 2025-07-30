#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# SOLID：Dependence Inversion Principle(依賴倒置原則)

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定義抽象類別和抽象方法

class Animal(metaclass=ABCMeta):
    """動物"""

    def __init__(self, name):
        self._name = name

    def eat(self, food):
        if(self.checkFood(food)):
            print(self._name + "吃" + food.getName())
        else:
            print(self._name + "不吃" + food.getName())

    @abstractmethod
    def checkFood(self, food):
        """檢查哪些食物能吃"""
        pass


class Dog(Animal):
    """狗"""

    def __init__(self):
        super().__init__("狗")

    def checkFood(self, food):
        return food.category() == "肉品"


class Swallow(Animal):
    """燕子"""

    def __init__(self):
        super().__init__("燕子")

    def checkFood(self, food):
        return food.category() == "昆蟲"


class Food(metaclass=ABCMeta):
    """食物"""

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    @abstractmethod
    def category(self):
        """食物類別"""
        pass

    @abstractmethod
    def nutrient(self):
        """營養成分"""
        pass


class Meat(Food):
    """肉"""

    def __init__(self):
        super().__init__("肉")

    def category(self):
        return "肉品"

    def nutrient(self):
        return "蛋白質、脂肪"


class Worm(Food):
    """蟲子"""

    def __init__(self):
        super().__init__("蟲子")

    def category(self):
        return "昆蟲"

    def nutrient(self):
        return "蛋白質含微量元素"
    
if __name__ == "__main__":
    dog = Dog()
    swallow = Swallow()
    meat = Meat()
    worm = Worm()
    dog.eat(meat)
    dog.eat(worm)
    swallow.eat(meat)
    swallow.eat(worm)
    # 動物抽象出一個父類別Animal
    # 食物也抽象出一個父類別Food