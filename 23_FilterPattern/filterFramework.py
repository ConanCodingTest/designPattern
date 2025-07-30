#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# Filter pattern framework

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod用于定义抽象基类和抽象方法

class Filter(metaclass=ABCMeta):
    """篩檢器"""

    @abstractmethod
    def doFilter(self, elements):
        """過濾方法"""
        pass


class FilterChain(Filter):
    """篩檢程式鏈"""

    def __init__(self):
        self._filters = []

    def addFilter(self, filter):
        self._filters.append(filter)

    def removeFilter(self, filter):
        self._filters.remove(filter)

    def doFilter(self, elements):
        for filter in self._filters:
            elements = filter.doFilter(elements)
        return elements