#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# Visitor pattern implement

# Version 1.0
#====================================================================
from visitor import DataNode, Visitor, ObjectStructure

class DesignPatternBook(DataNode):
    """《從生活的角度解讀設計模式》"""

    def getName(self):
        return "《從生活的角度解讀設計模式》"


class Engineer(Visitor):
    """工程師"""

    def visit(self, book):
        print("技術狗讀%s後的感受：能抓住模式的核心思想，深入淺出！" % book.getName())


class ProductManager(Visitor):
    """產品經理"""

    def visit(self, book):
        print("產品經理讀%s後的感受：配圖非常有趣，文章很有層次感！" % book.getName())


class OtherFriend(Visitor):
    """IT圈外的朋友"""

    def visit(self, book):
        print("IT圈外的朋友讀%s後的感受：技術的内容無法以解，但故事很精彩，像是看小說或是故事集！"
            % book.getName())
        
if __name__ == "__main__":
    book = DesignPatternBook()
    objMgr = ObjectStructure()
    objMgr.add(book)
    objMgr.action(Engineer())
    objMgr.action(ProductManager())
    objMgr.action(OtherFriend())
