#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# Visitor pattern template

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod用于定义抽象基类和抽象方法

class DataNode(metaclass=ABCMeta):
    """數據結構類"""

    def accept(self, visitor):
        """接受訪問者的訪問"""
        visitor.visit(self)

class Visitor(metaclass=ABCMeta):
    """訪問者"""

    @abstractmethod
    def visit(self, data):
        """對數據對象的訪問操作"""
        pass


class ObjectStructure:
    """數據結構的管理類，也是數據對象的一個容器，可遍歷容器内的所有元素"""

    def __init__(self):
        self.__datas = []

    def add(self, dataElement):
        self.__datas.append(dataElement)

    def action(self, visitor):
        """進行數據訪問的操作"""
        for data in self.__datas:
            data.accept(visitor)
