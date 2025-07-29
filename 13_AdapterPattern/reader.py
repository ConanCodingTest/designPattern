#!/usr/bin/python
# Author: Conan Yu
# Date: 11/29/2017
# Adapter pattern implementation

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和方法
import os
# 引入os模組來處理文件和目錄操作

class Page:
    """電子書一頁的內容"""
    def __init__(self, pageNum):
        self.__pageNum = pageNum

    def getContent(self):
        return "第 " + str(self.__pageNum) + " 頁的內容..."


class Catalogue:
    """目錄結構"""

    def __init__(self, title):
        self.__title = title
        self.__chapters = []

    def addChapter(self, title):
        self.__chapters.append(title)

    def showInfo(self):
        print("書名：" + self.__title)
        print("目錄:")
        for chapter in self.__chapters:
            print("    " + chapter)


class IBook(metaclass=ABCMeta):
    """電子書(Target)接口類"""

    @abstractmethod
    def parseFile(self, filePath):
        """解析文檔"""
        pass

    @abstractmethod
    def getCatalogue(self):
        """獲取目錄"""
        pass

    @abstractmethod
    def getPageCount(self):
        """獲取頁數"""
        pass

    @abstractmethod
    def getPage(self, pageNum):
        """獲取第pageNum頁的內容"""
        pass


class TxtBook(IBook):
    """TXT檔解析類"""

    def parseFile(self, filePath):
        # 模擬文檔解析
        print(filePath + " 文件解析成功")
        self.__title = os.path.splitext(filePath)[0]
        self.__pageCount = 500
        return True

    def getCatalogue(self):
        catalogue = Catalogue(self.__title)
        catalogue.addChapter("第一章 標題")
        catalogue.addChapter("第二章 標題")
        return catalogue

    def getPageCount(self):
        return self.__pageCount

    def getPage(self, pageNum):
        return Page(pageNum)


class EpubBook(IBook):
    """Epub解析類"""

    def parseFile(self, filePath):
        # 模擬文檔解析
        print(filePath + " 文件解析成功")
        self.__title = os.path.splitext(filePath)[0]
        self.__pageCount = 800
        return True

    def getCatalogue(self):
        catalogue = Catalogue(self.__title)
        catalogue.addChapter("第一章 標題")
        catalogue.addChapter("第二章 標題")
        return catalogue

    def getPageCount(self):
        return self.__pageCount

    def getPage(self, pageNum):
        return Page(pageNum)


class Outline:
    """第三方PDF解析庫的目錄類"""
    def __init__(self):
        self.__outlines = []

    def addOutline(self, title):
        self.__outlines.append(title)

    def getOutlines(self):
        return self.__outlines


class PdfPage:
    "PDF頁"

    def __init__(self, pageNum):
        self.__pageNum = pageNum

    def getPageNum(self):
        return self.__pageNum


class ThirdPdf:
    """第三方PDF解析庫(Adaptee)"""

    def __init__(self):
        self.__pageSize = 0
        self.__title = ""

    def open(self, filePath):
        print("第三方庫解析PDF文件：" + filePath)
        self.__title = os.path.splitext(filePath)[0]
        self.__pageSize = 1000
        return True

    def getTitle(self):
        return self.__title

    def getOutline(self):
        outline = Outline()
        outline.addOutline("第一章 PDF電子書標題")
        outline.addOutline("第二章 PDF電子書標題")
        return outline

    def pageSize(self):
        return self.__pageSize

    def page(self, index):
        return PdfPage(index)


class PdfAdapterBook(ThirdPdf, IBook):
    """對第三方的PDF解析庫進行適配的類(Adapter)"""

    def __init__(self, thirdPdf):
        self.__thirdPdf = thirdPdf

    def parseFile(self, filePath):
        # 模拟文档的解析
        rtn = self.__thirdPdf.open(filePath)
        if(rtn):
            print(filePath + "文件解析成功")
        return rtn

    def getCatalogue(self):
        outline = self.getOutline()
        print("將Outline結構的目錄轉換成Catalogue結構的目錄")
        catalogue = Catalogue(self.__thirdPdf.getTitle())
        for title in outline.getOutlines():
            catalogue.addChapter(title)
        return catalogue

    def getPageCount(self):
        return self.__thirdPdf.pageSize()

    def getPage(self, pageNum):
        page = self.page(pageNum)
        print("將PdfPage的面對象轉換成Page的對象")
        return Page(page.getPageNum())


class Reader:
    "閱讀器(Client)類"

    def __init__(self, name):
        self.__name = name
        self.__filePath = ""
        self.__curBook = None
        self.__curPageNum = -1

    def __initBook(self, filePath):
        self.__filePath = filePath
        extName = os.path.splitext(filePath)[1]
        if(extName.lower() == ".epub"):
            self.__curBook = EpubBook()
        elif(extName.lower() == ".txt"):
            self.__curBook = TxtBook()
        elif(extName.lower() == ".pdf"):
            self.__curBook = PdfAdapterBook(ThirdPdf())
        else:
            self.__curBook = None

    def openFile(self, filePath):
        self.__initBook(filePath)
        if(self.__curBook is not None):
            rtn = self.__curBook.parseFile(filePath)
            if(rtn):
                self.__curPageNum = 1
            return rtn
        return False

    def closeFile(self):
        print("關閉 " + self.__filePath + " 文件")
        return True

    def showCatalogue(self):
        catalogue = self.__curBook.getCatalogue()
        catalogue.showInfo()

    def prePage(self):
        print("往前翻一页：", end="")
        return self.gotoPage(self.__curPageNum - 1)

    def nextPage(self):
        print("往後翻一页：", end="")
        return self.gotoPage(self.__curPageNum + 1)

    def gotoPage(self, pageNum):
        if(pageNum > 1 and pageNum < self.__curBook.getPageCount() -1):
            self.__curPageNum = pageNum

        print("顯示第" + str(self.__curPageNum) + "頁")
        page = self.__curBook.getPage(self.__curPageNum)
        page.getContent()
        return page

if __name__ == "__main__":
    reader = Reader("電子書閱讀器")
    txtFilePath = "sample.txt"
    epubFilePath = "sample.epub"
    pdfFilePath = "sample.pdf"
    if(reader.openFile(txtFilePath)):
        reader.showCatalogue()
        reader.prePage()
        reader.gotoPage(2)
        reader.nextPage()
        reader.closeFile()
    else:
        print("無法打開文件：" + txtFilePath)
    print()

    if(reader.openFile(epubFilePath)):
        reader.showCatalogue()
        reader.prePage()
        reader.gotoPage(2)
        reader.nextPage()
        reader.closeFile()
    else:
        print("無法打開文件：" + epubFilePath)
    print()
    
    if(reader.openFile(pdfFilePath)):
        reader.showCatalogue()
        reader.prePage()
        reader.gotoPage(2)
        reader.nextPage()
        reader.closeFile()
    else:
        print("無法打開文件：" + pdfFilePath)