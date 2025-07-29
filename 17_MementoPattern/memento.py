#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# Memento pattern template

# Version 1.0
#====================================================================
from copy import deepcopy

class Memento:
    """備忘錄類"""

    def setAttributes(self, dict):
        """deepcopy字典dict中的所有屬性"""
        self.__dict__ = deepcopy(dict)

    def getAttributes(self):
        """獲取屬性字典"""
        return self.__dict__


class Caretaker:
    """備忘錄管理類別"""

    def __init__(self):
        self._mementos = {}

    def addMemento(self, name, memento):
        self._mementos[name] = memento

    def getMemento(self, name):
        return self._mementos[name]

class Originator:
    """備份發起人"""

    def createMemento(self):
        memento = Memento()
        memento.setAttributes(self.__dict__)
        return memento

    def restoreFromMemento(self, memento):
        self.__dict__.update(memento.getAttributes())
