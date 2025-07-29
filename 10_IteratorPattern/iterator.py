#!/usr/bin/python
# Author: Conan Yu
# Date: 11/29/2017
# Iterator pattern implementation

# Version 1.0
#====================================================================

class BaseIterator:
    """迭代器"""

    def __init__(self, data):
        self.__data = data
        self.toBegin()

    def toBegin(self):
        """將指針移至起始位置"""
        self.__curIdx = -1

    def toEnd(self):
        """將指針移至結尾位置"""
        self.__curIdx = len(self.__data)

    def next(self):
        """移動至下一個元素"""
        if (self.__curIdx < len(self.__data) - 1):
            self.__curIdx += 1
            return True
        else:
            return False

    def previous(self):
        "移動至上一個元素"
        if (self.__curIdx > 0):
            self.__curIdx -= 1
            return True
        else:
            return False

    def current(self):
        """獲取當前元素"""
        return self.__data[self.__curIdx] if (self.__curIdx < len(self.__data) and self.__curIdx >= 0) else None
    
if __name__ == "__main__":
    # test the iterator
    print("從前往後iterator")
    iterator = BaseIterator(range(10))

    while iterator.next():
        customer = iterator.current()
        print(customer, end=" ")
    print()
    print("從後往前iterator")
    iterator.toEnd()
    while iterator.previous():
        customer = iterator.current()
        print(customer, end=" ")
