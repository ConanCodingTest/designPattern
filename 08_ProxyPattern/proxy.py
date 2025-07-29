#!/usr/bin/python
# Author: Conan Yu
# Date: 11/29/2017
# Proxy pattern template

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod模塊來定義抽象類別與抽象方法

class Subject(metaclass=ABCMeta):
    """抽象主題類別"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def request(self, content = ''):
        pass


class RealSubject(Subject):
    """真實主題類別"""

    def request(self, content):
        print("RealSubject todo something...")


class ProxySubject(Subject):
    """代理主題類別"""

    def __init__(self, name, subject):
        super().__init__(name)
        self._realSubject = subject

    def request(self, content = ''):
        self.preRequest()
        if(self._realSubject is not None):
            self._realSubject.request(content)
        self.afterRequest()

    def preRequest(self):
        print("preRequest")

    def afterRequest(self):
        print("afterRequest")