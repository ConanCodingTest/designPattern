#!/usr/bin/python
# Author: Conan Yu
# Date: 11/29/2017
# Builder pattern implementation

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和方法

class Toy(metaclass=ABCMeta):
    """玩具"""

    def __init__(self, name):
        self._name = name
        self.__components = []

    def getName(self):
        return self._name

    def addComponent(self, component, count = 1, unit = "個"):
        self.__components.append([component, count, unit])
        # print("%s 增加了 %d %s%s" % (self._name, count, unit, component) );

    @abstractmethod
    def feature(self):
        pass


class Car(Toy):
    """車"""

    def feature(self):
        print("我是 %s，我速度很快……" % self._name)


class Manor(Toy):
    """莊園"""

    def feature(self):
        print("我是 %s，我可供觀賞，也可用來遊玩！" % self._name)


class ToyBuilder(metaclass=ABCMeta):
    """玩具建構者"""

    @abstractmethod
    def buildProduct(self):
        pass


class CarBuilder(ToyBuilder):
    """車的建構類"""

    def buildProduct(self):
        car = Car("玩具車")
        print("正在建構 %s ……" % car.getName())
        car.addComponent("輪胎", 4)
        car.addComponent("車身", 1)
        car.addComponent("引擎", 1)
        car.addComponent("方向盤")
        return car


class ManorBuilder(ToyBuilder):
    """莊園的建構類"""

    def buildProduct(self):
        manor = Manor("玩具莊園")
        print("正在建構 %s ……" % manor.getName())
        manor.addComponent('客廳', 1, "間")
        manor.addComponent('臥室', 2, "間")
        manor.addComponent("書房", 1, "間")
        manor.addComponent("廚房", 1, "間")
        manor.addComponent("花園", 1, "座")
        manor.addComponent("圍牆", 1, "堵")
        return manor

class BuilderMgr:
    """建構類的管理器"""

    def __init__(self):
        self.__carBuilder = CarBuilder()
        self.__manorBuilder = ManorBuilder()

    def buildCar(self, num):
        count = 0
        products = []
        while(count < num):
            car = self.__carBuilder.buildProduct()
            products.append(car)
            count +=1
            print("建造完成第 %d 輛 %s" % (count, car.getName()) )
        return products

    def buildManor(self, num):
        count = 0
        products = []
        while (count < num):
            manor = self.__manorBuilder.buildProduct()
            products.append(manor)
            count += 1
            print("建造完成第 %d 座 %s" % (count, manor.getName()))
        return products
    
if __name__ == "__main__":
    # 測試建構者模式
    builderMgr = BuilderMgr()
    cars = builderMgr.buildCar(3)
    print()

    manors = builderMgr.buildManor(2)