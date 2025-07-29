#!/usr/bin/python
# Author: Conan Yu
# Date: 11/29/2017
# Facade pattern implementation

# Version 1.0
#====================================================================

from os import path
# 引入os模塊來處理文件和目錄路徑
import logging
# 引入logging模塊來進行日誌記錄

class ZIPModel:
    """ZIP模塊，負責ZIP文件的壓縮與解壓縮
    簡單模擬，不進行具體壓縮與解壓縮邏輯"""

    def compress(self, srcFilePath, dstFilePath):
        print("ZIP模塊正在進行“%s”文件的壓縮......" % srcFilePath)
        print("文件壓縮成功，已保存至“%s”" % dstFilePath)

    def decompress(self, srcFilePath, dstFilePath):
        print("ZIP模塊正在進行“%s”文件的壓縮......" % srcFilePath)
        print("文件壓縮成功，已保存至“%s”" % dstFilePath)


class RARModel:
    """RAR模塊，負責ZIP文件的壓縮與解壓縮
    簡單模擬，不進行具體壓縮與解壓縮邏輯"""

    def compress(self, srcFilePath, dstFilePath):
        print("RAR模塊正在進行“%s”文件的壓縮......" % srcFilePath)
        print("文件壓縮成功，已保存至“%s”" % dstFilePath)

    def decompress(self, srcFilePath, dstFilePath):
        print("RAR模塊正在進行“%s”文件的壓縮......" % srcFilePath)
        print("文件壓縮成功，已保存至“%s”" % dstFilePath)


class ZModel:
    """7Z模塊，負責ZIP文件的壓縮與解壓縮
    簡單模擬，不進行具體壓縮與解壓縮邏輯"""

    def compress(self, srcFilePath, dstFilePath):
        print("7Z模塊正在進行“%s”文件的壓縮......" % srcFilePath)
        print("文件壓縮成功，已保存至“%s”" % dstFilePath)

    def decompress(self, srcFilePath, dstFilePath):
        print("7Z模塊正在進行“%s”文件的壓縮......" % srcFilePath)
        print("文件壓縮成功，已保存至“%s”" % dstFilePath)


class CompressionFacade:
    """壓縮系統的外觀類，提供統一的接口來進行壓縮和解壓縮操作"""

    def __init__(self):
        self.__zipModel = ZIPModel()
        self.__rarModel = RARModel()
        self.__zModel = ZModel()

    def compress(self, srcFilePath, dstFilePath, type):
        """根據不同的壓縮類型，壓縮成不同的格式"""
        # 獲取源文件的拓展名
        extName = "." + type
        fullName = dstFilePath + extName
        if (type.lower() == "zip") :
            self.__zipModel.compress(srcFilePath, fullName)
        elif(type.lower() == "rar"):
            self.__rarModel.compress(srcFilePath, fullName)
        elif(type.lower() == "7z"):
            self.__zModel.compress(srcFilePath, fullName)
        else:
            logging.error("Not support this format:" + str(type))
            return False
        return True

    def decompress(self, srcFilePath, dstFilePath):
        """從srcFilePath中，根具不同的拓展名，進行不同格式的解壓縮"""
        baseName = path.basename(srcFilePath)
        extName = baseName.split(".")[1]
        if (extName.lower() == "zip") :
            self.__zipModel.decompress(srcFilePath, dstFilePath)
        elif(extName.lower() == "rar"):
            self.__rarModel.decompress(srcFilePath, dstFilePath)
        elif(extName.lower() == "7z"):
            self.__zModel.decompress(srcFilePath, dstFilePath)
        else:
            logging.error("Not support this format:" + str(extName))
            return False
        return True
    
if __name__ == "__main__":
    # 測試壓縮系統
    facade = CompressionFacade()
    
    # 測試zip壓縮和解壓縮
    facade.compress("test.txt", "test_compressed", "zip")
    facade.decompress("test_compressed.zip", "test_decompressed")
    print("====================================")
    # 測試rar壓縮和解壓縮
    facade.compress("test.txt", "test_compressed", "rar")
    facade.decompress("test_compressed.rar", "test_decompressed")
    print("====================================")
    # 測試7z壓縮和解壓縮
    facade.compress("test.txt", "test_compressed", "7z")
    facade.decompress("test_compressed.7z", "test_decompressed")
