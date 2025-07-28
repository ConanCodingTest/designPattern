#!/usr/bin/python
# Author: Conan Yu
# Date: 11/26/2017

# Version 1.0
#====================================================================
from clone import Clone

class Person(Clone):
    """人"""

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def showMyself(self):
        print("我是" + self.__name + ",年紀" + str(self.__age) + ".")

    def coding(self):
        print("我是碼農，我用程式改變世界，Coding...")

    def reading(self):
        print("閱讀使我快樂!知識使我成長!...")

    def fallInLove(self):
        print("一見鍾情...")

if __name__ == "__main__":
    """測試Clone Pattern"""
    person1 = Person("Tony", 27)
    person1.showMyself()
    person1.coding()

    # 使用clone方法
    person2 = person1.clone()
    person2.showMyself()
    person2.reading()
    
    # 使用deepClone方法
    person3 = person1.clone()
    person3.showMyself()
    person3.fallInLove()