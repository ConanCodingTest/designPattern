#!/usr/bin/python
# Author: Conan Yu
# Date: 11/29/2017
# Composite pattern implementation

# Version 1.0
#====================================================================
import os
from composite import Component, Composite

class FileDetail(Component):
    """文件詳情"""
    def __init__(self, name):
        super().__init__(name)
        self._size = 0

    def setSize(self, size):
        self._size = size

    def getFileSize(self):
        return self._size

    def feature(self, indent):
        # 文件大小，單位：KB，精確度：小數2位
        fileSize = round(self._size / float(1024), 2)
        print("文件名称：%s， 文件大小：%sKB" % (self._name, fileSize) )


class FolderDetail(Composite):
    """資料夾詳情"""

    def __init__(self, name):
        super().__init__(name)
        self._count = 0

    def setCount(self, fileNum):
        self._count = fileNum

    def getCount(self):
        return self._count

    def feature(self, indent):
        print("資料夾：%s， 文件數量：%d。包含的文件：" % (self._name, self._count) )
        super().feature(indent)


def scanDir(rootPath, folderDetail):
    """掃描資料夾內所有文件和子資料夾"""
    if not os.path.isdir(rootPath):
        raise ValueError("rootPath不是有效的路徑：%s" % rootPath)

    if folderDetail is None:
        raise ValueError("folderDetail不能為空!")


    fileNames = os.listdir(rootPath)
    for fileName in fileNames:
        filePath = os.path.join(rootPath, fileName)
        if os.path.isdir(filePath):
            folder = FolderDetail(fileName)
            scanDir(filePath, folder)
            folderDetail.addComponent(folder)
        else:
            fileDetail = FileDetail(fileName)
            fileDetail.setSize(os.path.getsize(filePath))
            folderDetail.addComponent(fileDetail)
            folderDetail.setCount(folderDetail.getCount() + 1)

if __name__ == "__main__":
    # 測試Composite模式
    rootFolder = FolderDetail("D:/Object Oriented Programming")
    scanDir(".", rootFolder)
    print("掃描結果：")
    rootFolder.feature("")
    print("掃描完成。") 
