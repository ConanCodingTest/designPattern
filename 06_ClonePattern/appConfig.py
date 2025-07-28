#!/usr/bin/python
# Author: Conan Yu
# Date: 11/26/2017

# Version 1.0
#====================================================================
"""Copy and clone pattern implementation"""

from clone import Clone

class AppConfig(Clone):
    """Application configuration class that implements clone pattern"""

    def __init__(self, configName):
        self.__configName = configName
        self.parseFromFile("./config/default.xml")

    def parseFromFile(self, filePath):
        """
        從配置文件中解析配置項
        真實項目通過將配置保存在配置文件中，保證下次開啟依舊有效；
        以初始化方式模擬。
        """
        self.__fontType = "標楷體"
        self.__fontSize = 14
        self.__language = "中文"
        self.__logPath = "./logs/appException.log"

    def saveToFile(self, filePath):
        """
        將配置保存在配置文件中，此處不實例化具體的保存邏輯
        """
        pass

    def copyConfig(self, configName):
        """創建配置副本"""
        config = self.deepClone()
        config.__configName = configName
        return config

    def showInfo(self):
        print("%s 的配置訊息如下：" % self.__configName)
        print("字體：", self.__fontType)
        print("大小：", self.__fontSize)
        print("語言：", self.__language)
        print("異常檔案的路徑：", self.__logPath)

    def setFontType(self, fontType):
        self.__fontType = fontType

    def setFontSize(self, fontSize):
        self.__fontSize = fontSize

    def setLanguage(self, language):
        self.__language = language

    def setLogPath(self, logPath):
        self.__logPath = logPath

if __name__ == "__main__":
    """測試clone pattern"""
    appConfig = AppConfig("DefaultConfig")
    appConfig.showInfo()
    print()

    # 創建配置副本
    appConfigCopy = appConfig.copyConfig("CopyConfig")
    appConfigCopy.setFontType("黑體")
    appConfigCopy.setFontSize(18)
    appConfigCopy.showInfo()
