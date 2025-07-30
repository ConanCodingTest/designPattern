#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# Callback pattern implement

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod用于定义抽象基类和抽象方法

class Strategy(metaclass=ABCMeta):
    """算法的抽象類別"""

    @abstractmethod
    def algorithm(self, *args, **kwargs):
        """定義算法"""
        pass

class StrategyA(Strategy):
    """策略A"""

    def algorithm(self, *args, **kwargs):
        print("算法A的實現...")

class StrategyB(Strategy):
    """策略B"""

    def algorithm(self, *args, **kwargs):
        print("算法B的實現...")

class Context:
    """上下文環境類"""

    def interface(self, strategy, *args, **kwargs):
        """交互介面"""
        print("回檔執行前的操作")
        strategy.algorithm()
        print("回檔執行後的操作")

if __name__ == "__main__":
    context = Context()
    context.interface(StrategyA())
    context.interface(StrategyB())
