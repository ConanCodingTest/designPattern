#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# Strategy pattern implementation

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和方法
from enum import Enum
# 引入Enum來定義枚舉類型

class PenType(Enum):
    """筆類型"""
    PenTypeLine = 1
    PenTypeRect = 2
    PenTypeEllipse = 3


class Pen(metaclass=ABCMeta):
    """筆"""

    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def getType(self):
        pass

    def getName(self):
        return self.__name


class LinePen(Pen):
    """畫直線的筆"""

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeLine

class RectanglePen(Pen):
    """畫矩形的筆"""

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeRect


class EllipsePen(Pen):
    """畫橢圓的筆"""

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeEllipse


class PenFactory:
    """筆工廠類別"""

    def __init__(self):
        "定義一个字典(key:PenType，value：Pen)來存放象,确保每一个類型只會有一個對象"
        self.__pens = {}

    def getSingleObj(self, penType, name):
        """獲得唯一實例的對象"""


    def createPen(self, penType):
        """創建畫筆"""
        if (self.__pens.get(penType) is None):
            # 如果該對象不存在，則創建一個對象並存到字典中
            if penType == PenType.PenTypeLine:
                pen = LinePen("畫直線的筆")
            elif penType == PenType.PenTypeRect:
                pen = RectanglePen("畫矩形的筆")
            elif penType == PenType.PenTypeEllipse:
                pen = EllipsePen("畫橢圓的筆")
            else:
                raise ValueError(f"Unknown PenType: {penType}")
            self.__pens[penType] = pen
        # 否則直接返回字典中的對象
        return self.__pens[penType]
    
if __name__ == "__main__": 
    # 測試筆工廠
    penFactory = PenFactory()
    
    penType = PenType.PenTypeLine
    pen = penFactory.createPen(penType)
    print("創建的筆名稱：%s，類型：%s" % (pen.getName(), pen.getType()))

    penType = PenType.PenTypeRect
    pen = penFactory.createPen(penType)
    print("創建的筆名稱：%s，類型：%s" % (pen.getName(), pen.getType()))

    penType = PenType.PenTypeEllipse
    pen = penFactory.createPen(penType)
    print("創建的筆名稱：%s，類型：%s" % (pen.getName(), pen.getType()))