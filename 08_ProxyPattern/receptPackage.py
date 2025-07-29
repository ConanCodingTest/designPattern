#!/usr/bin/python
# Author: Conan Yu
# Date: 11/29/2017
# Proxy pattern implementation

# Version 1.0
#====================================================================
from proxy import Subject, RealSubject, ProxySubject

class TonyReception(Subject):
    """Tony接收"""

    def __init__(self, name, phoneNum):
        super().__init__(name)
        self.__phoneNum = phoneNum

    def getPhoneNum(self):
        return self.__phoneNum

    def request(self, content):
        print("貨物主人：%s，手機號碼：%s" % (self.getName(), self.getPhoneNum()))
        print("接收到一个包裹，包裹内容：%s" % str(content))


class WendyReception(ProxySubject):
    """Wendy代收"""

    def __init__(self, name, receiver):
        super().__init__(name, receiver)

    def preRequest(self):
        print("我是%s的朋友，我幫他代收快遞！" % (self._realSubject.getName() + ""))

    def afterRequest(self):
        print("代收人：%s" % self.getName())

if __name__ == "__main__":
    # 真實主題
    realSubject = TonyReception("Tony", "123456789")
    # 代理主題
    proxySubject = WendyReception("Wendy", realSubject)

    # 發起請求
    proxySubject.request("這是一個包裹，裡面有書籍和文具。")
