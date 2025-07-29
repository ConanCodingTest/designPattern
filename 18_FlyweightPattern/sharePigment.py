#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# Flyweight pattern implementation

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod用于定义抽象基类和抽象方法

class Flyweight(metaclass=ABCMeta):
    """享元類"""

    @abstractmethod
    def operation(self, extrinsicState):
        pass

class FlyweightImpl(Flyweight):
    """享元類別的具體實現類別"""

    def __init__(self, color):
        self.__color = color

    def operation(self, extrinsicState):
        print("%s 取得 %s色顏料" % (extrinsicState, self.__color))

class FlyweightFactory:
    """享元工廠類別"""

    def __init__(self):
        self.__flyweights = {}

    def getFlyweight(self, key):
        pigment = self.__flyweights.get(key)
        if pigment is None:
            pigment = FlyweightImpl(key)
        return pigment
    
if __name__ == "__main__":
    # 測試享元模式
    factory = FlyweightFactory()
    
    # 獲取紅色顏料
    redPigment = factory.getFlyweight("紅色")
    redPigment.operation("畫筆1")
    
    # 獲取藍色顏料
    bluePigment = factory.getFlyweight("藍色")
    bluePigment.operation("畫筆2")
    
    # 再次獲取紅色顏料，應該是同一個實例
    anotherRedPigment = factory.getFlyweight("紅色")
    anotherRedPigment.operation("畫筆3")  # 應該與redPigment相同