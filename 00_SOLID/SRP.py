#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# SOLID：Single Responsibility Principle(單一職責原則)

# Version 1.0
#====================================================================

class TerrestrialAnimal():
    """陸生動物"""

    def __init__(self, name):
        self.__name = name

    def running(self):
        print(self.__name + "在地上跑...")


class AquaticAnimal():
    """水生動物"""

    def __init__(self, name):
        self.__name = name

    def swimming(self):
        print(self.__name + "在水中游...")

if __name__ == "__main__":
    TerrestrialAnimal("Dog").running()
    AquaticAnimal("Fish").swimming()
    # 影響動物的因素有陸地與水生兩種，依據職責分為兩個類別