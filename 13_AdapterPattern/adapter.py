#!/usr/bin/python
# Author: Conan Yu
# Date: 11/29/2017
# Adapter pattern template

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和方法
class Target(metaclass=ABCMeta):
    """目標類別"""

    @abstractmethod
    def function(self):
        pass


class Adaptee:
    """被適配的對象"""

    def speciaficFunction(self):
        print("被適配對象的特殊功能")

class Adapter(Target):
    """適配器"""

    def __init__(self, adaptee):
        self.__adaptee = adaptee

    def function(self):
        print("進行功能的轉換")
        self.__adaptee.speciaficFunction()