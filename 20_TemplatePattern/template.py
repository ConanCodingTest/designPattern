#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# Template pattern template

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod用于定义抽象基类和抽象方法

class Template(metaclass=ABCMeta):
    """模板類別(抽象類別)"""

    @abstractmethod
    def stepOne(self):
        pass

    @abstractmethod
    def stepTwo(self):
        pass

    @abstractmethod
    def stepThree(self):
        pass

    def templateMethold(self):
        """模板方法"""
        self.stepOne()
        self.stepTwo()
        self.stepThree()


class TemplateImplA(Template):
    """模板實現類別A"""

    def stepOne(self):
        print("步驟一")

    def stepTwo(self):
        print("步驟二")

    def stepThree(self):
        print("步驟三")


class TemplateImplB(Template):
    """模板實現類別B"""

    def stepOne(self):
        print("Step one")

    def stepTwo(self):
        print("Step two")

    def stepThree(self):
        print("Step three")

if __name__ == "__main__":
    templateA = TemplateImplA()
    templateA.templateMethold()
    templateB = TemplateImplB()
    templateB.templateMethold()