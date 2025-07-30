#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# Template pattern implement

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod用于定义抽象基类和抽象方法

class ReaderView(metaclass=ABCMeta):
    """閱讀器視圖類"""

    def __init__(self):
        self.__curPageNum = 1

    def getPage(self, pageNum):
        self.__curPageNum = pageNum
        return "第" + str(pageNum) + "的内容"

    def prePage(self):
        """模板方法，往前翻一頁"""
        content = self.getPage(self.__curPageNum - 1)
        self._displayPage(content)

    def nextPage(self):
        """模板方法，往後翻一頁"""
        content = self.getPage(self.__curPageNum + 1)
        self._displayPage(content)

    @abstractmethod
    def _displayPage(self, content):
        """翻頁效果"""
        pass


class SmoothView(ReaderView):
    """左右平滑的視圖"""

    def _displayPage(self, content):
        print("左右平滑:" + content)


class SimulationView(ReaderView):
    """仿真翻頁的視圖"""

    def _displayPage(self, content):
        print("仿真翻頁:" + content)

if __name__ =="__main__":
    smoothView = SmoothView()
    smoothView.nextPage()
    smoothView.prePage()

    simulationView = SimulationView()
    simulationView.nextPage()
    simulationView.prePage()
