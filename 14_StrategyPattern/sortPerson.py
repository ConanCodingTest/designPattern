#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# Strategy pattern implementation

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和方法

class Person:
    """人的類別"""

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def showMysef(self):
        print("%s 年齡：%d歲，體重：%0.2fkg，身高：%0.2fm" % (self.name, self.age, self.weight, self.height) )


class ICompare(metaclass=ABCMeta):
    """比較算法"""

    @abstractmethod
    def comparable(self, person1, person2):
        "person1 > person2 返回值>0，person1 == person2 返回0， person1 < person2 返回值<0"
        pass


class CompareByAge(ICompare):
    """年齡排序"""

    def comparable(self, person1, person2):
        return person1.age - person2.age


class CompareByHeight(ICompare):
    """身高排序"""

    def comparable(self, person1, person2):
        return person1.height - person2.height


class CompareByHeightAndWeight(ICompare):
    """根據身高和體重的綜合情况来排序
    (身高和體重的權重分別是0.6和0.4)"""

    def comparable(self, person1, person2):
        value1 = person1.height * 0.6 + person1.weight * 0.4
        value2 = person2.height * 0.6 + person2.weight * 0.4
        return value1 - value2


class SortPerson:
    "Person的排序類別"

    def __init__(self, compare):
        self.__compare = compare

    def sort(self, personList):
        """排序算法，這裡採用最簡單的冒泡排序"""
        n = len(personList)
        for i in range(0, n-1):
            for j in range(0, n-i-1):
                if(self.__compare.comparable(personList[j], personList[j+1]) > 0):
                    tmp = personList[j]
                    personList[j] = personList[j+1]
                    personList[j+1] = tmp
            j += 1
        i += 1

if __name__ == "__main__":
    # 測試
    personList = [
        Person("Conan", 30, 70.5, 1.75),
        Person("Alice", 25, 55.0, 1.65),
        Person("Bob", 28, 80.0, 1.80),
        Person("Diana", 22, 50.0, 1.60)
    ]

    print("原始列表:")
    for person in personList:
        person.showMysef()

    # 按年齡排序
    sortByAge = SortPerson(CompareByAge())
    sortByAge.sort(personList)
    print("\n按年齡排序後:")
    for person in personList:
        person.showMysef()

    # 按身高排序
    sortByHeight = SortPerson(CompareByHeight())
    sortByHeight.sort(personList)
    print("\n按身高排序後:")
    for person in personList:
        person.showMysef()

    # 按身高和體重綜合排序
    sortByHeightAndWeight = SortPerson(CompareByHeightAndWeight())
    sortByHeightAndWeight.sort(personList)
    print("\n按身高和體重綜合排序後:")
    for person in personList:
        person.showMysef()
