#!/usr/bin/python
# Author: Conan Yu
# Date: 11/29/2017
# chainOfResponsibility pattern implementation

# Version 1.0
#====================================================================
from chainOfResponsibility import Responsible, Request

class Person:
    """申請人(請假人)類別"""

    def __init__(self, name):
        self.__name = name
        self.__leader = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setLeader(self, leader):
        self.__leader = leader

    def getLeader(self):
        return self.__leader

    def sendReuqest(self, request):
        print("%s 請假申請 %d 天。請假事由：%s" % (self.__name, request.getDayOff(), request.getReason()))
        if (self.__leader is not None):
            self.__leader.handleRequest(request)


class Supervisor(Responsible):
    """主管"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        if (request.getDayOff() <= 2):
            print("同意 %s 請假，審核人：%s(%s)" % (request.getName(), self.getName(), self.getTitle()))


class DepartmentManager(Responsible):
    """部門總監"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        if (request.getDayOff() > 2 and request.getDayOff() <= 5):
            print("同意 %s 請假，審核人：%s(%s)" % (request.getName(), self.getName(), self.getTitle()))


class CEO(Responsible):
    """CEO"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        if (request.getDayOff() > 5 and request.getDayOff() <= 22):
            print("同意 %s 請假，審核人：%s(%s)" % (request.getName(), self.getName(), self.getTitle()))


class Administrator(Responsible):
    """行政人員"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        print("%s 的請假申請已完成！已備案處理。處理人：%s(%s)\n" % (request.getName(), self.getName(), self.getTitle()))

if __name__ == "__main__":
    # 建立申請人
    sunny = Person("Sunny")
    tony = Person("Tony")

    # 建立請假申請
    tonyRequest = Request(tony.getName(), 3, "出差")
    sunnyRequest = Request(sunny.getName(), 10, "出差")

    # 建立責任人
    supervisor = Supervisor("Alice", "主管")
    departmentManager = DepartmentManager("Bob", "部門總監")
    ceo = CEO("Charlie", "CEO")
    administrator = Administrator("Diana", "行政人員")

    # 設定責任鏈
    supervisor.setNextHandler(departmentManager)
    departmentManager.setNextHandler(ceo)
    ceo.setNextHandler(administrator)

    # 設定申請人的領導
    tony.setLeader(supervisor)
    sunny.setLeader(supervisor)

    # 發送請假申請
    tony.sendReuqest(tonyRequest)
    print()
    sunny.sendReuqest(sunnyRequest)