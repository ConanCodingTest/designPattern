#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# Memento pattern implementation

# Version 1.0
#====================================================================
from memento import Memento, Caretaker, Originator
import logging

class TerminalCmd(Originator):
    """终端命令"""

    def __init__(self, text):
        self.__cmdName = ""
        self.__cmdArgs = []
        self.parseCmd(text)

    def parseCmd(self, text):
        """從字串中解析命令"""
        subStrs = self.getArgumentsFromString(text, " ")
        # 獲取第一個欄位作為命令的名稱
        if(len(subStrs) > 0):
            self.__cmdName = subStrs[0]

        # 獲取第一個欄位之後所有字元作為命令的參數
        if (len(subStrs) > 1):
            self.__cmdArgs = subStrs[1:]

    def getArgumentsFromString(self, str, splitFlag):
        """通过splitFlag進行分割，獲得參數陣列"""

        if (splitFlag == ""):
            logging.warning("splitFlag 為空!")
            return ""

        data = str.split(splitFlag)
        result = []
        for item in data:
            item.strip()
            if (item != ""):
                result.append(item)

        return result;

    def showCmd(self):
        print(self.__cmdName, self.__cmdArgs)

class TerminalCaretaker(Caretaker):
    """終端命令的備忘錄管理類別"""

    def showHistoryCmds(self):
        """顯示歷史命令"""
        for key, obj in self._mementos.items():
            name = ""
            value = []
            if(obj._TerminalCmd__cmdName):
                name = obj._TerminalCmd__cmdName
            if(obj._TerminalCmd__cmdArgs):
                value = obj._TerminalCmd__cmdArgs
            print("第%s條命令: %s %s" % (key, name, value) )

if __name__ == "__main__":
    cmdIdx = 0
    caretaker = TerminalCaretaker()
    curCmd = TerminalCmd("")
    while (True):
        strCmd = input("请输入指令：");
        strCmd = strCmd.lower()
        if (strCmd.startswith("q")):
            exit(0)
        elif(strCmd.startswith("h")):
            caretaker.showHistoryCmds()
        # 透過"!"符號表示獲取歷史的某個指令
        elif(strCmd.startswith("!")):
            idx = int(strCmd[1:])
            curCmd.restoreFromMemento(caretaker.getMemento(idx))
            curCmd.showCmd()
        else:
            curCmd = TerminalCmd(strCmd)
            curCmd.showCmd()
            caretaker.addMemento(cmdIdx, curCmd.createMemento())
            cmdIdx +=1