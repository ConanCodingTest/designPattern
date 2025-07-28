#!/usr/bin/python
# Author: Conan Yu
# Date: 11/26/2017

# Version 1.0
#====================================================================

def singletonDecorator(cls, *args, **kwargs):
    """定義單例裝飾器"""
    instance = {}

    def wrapperSingleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapperSingleton

@singletonDecorator
class MyBeautifulGril(object):
    """我的漂亮女神"""

    def __init__(self, name):
        self.__name = name
        if self.__name == name:
            print("遇見" + name + "，我一見鍾情！")
        else:
            print("遇見" + name + "，我心如止水！")

    def showMyHeart(self):
        print(self.__name + "就我心中的唯一！")

if __name__ == "__main__":
    """測試單例模式"""
    jenny = MyBeautifulGril("Jenny")
    jenny.showMyHeart()
    kimi = MyBeautifulGril("Kimi")
    kimi.showMyHeart()
    print("id(jenny):", id(jenny), " id(kimi):", id(kimi))