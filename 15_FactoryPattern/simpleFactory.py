#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# Strategy pattern implementation

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和方法

class Coffee(metaclass=ABCMeta):
    """咖啡"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def getTaste(self):
        pass


class LatteCaffe(Coffee):
    """拿鐵咖啡"""

    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return "輕柔且香醇"

class MochaCoffee(Coffee):
    """摩卡咖啡"""

    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return "絲滑且醇厚"

class Coffeemaker:
    """咖啡機"""

    @staticmethod
    def makeCoffee(coffeeBean):
        "通過staticmethod裝飾器修飾來定義一個靜態方法"
        if(coffeeBean == "拿鐵咖啡豆"):
            coffee = LatteCaffe("拿鐵咖啡")
        elif(coffeeBean == "摩卡咖啡豆"):
            coffee = MochaCoffee("摩卡咖啡")
        else:
            raise ValueError("不支持的參數：%s" % coffeeBean)
        return coffee
    
if __name__ == "__main__":
    # 測試咖啡機
    coffeeBean = "拿鐵咖啡豆"
    coffee = Coffeemaker.makeCoffee(coffeeBean)
    print("製作的咖啡名稱：%s，味道：%s" % (coffee.getName(), coffee.getTaste()))

    coffeeBean = "摩卡咖啡豆"
    coffee = Coffeemaker.makeCoffee(coffeeBean)
    print("製作的咖啡名稱：%s，味道：%s" % (coffee.getName(), coffee.getTaste()))