#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# Command pattern implementation

# Version 1.0
#====================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和方法
import time
# 引入time模組進行時間控制

class GameRole:
    """遊戲的角色"""

    # 每次移動的步距
    STEP = 5

    def __init__(self, name):
        self.__name = name
        self.__x = 0
        self.__y = 0
        self.__z = 0

    def leftMove(self):
        self.__x -= self.STEP

    def rightMove(self):
        self.__x += self.STEP

    def upMove(self):
        self.__y += self.STEP

    def downMove(self):
        self.__y -= self.STEP

    def jumpMove(self):
        self.__z += self.STEP

    def squatMove(self):
        self.__z -= self.STEP

    def attack(self):
        print("%s發動攻擊..." % self.__name)

    def showPosition(self):
        print("%s的位置：(x:%s, y:%s, z:%s)" % (self.__name, self.__x, self.__y, self.__z) )

class GameCommand(metaclass=ABCMeta):
    """遊戲腳色的命令抽象類別"""

    def __init__(self, role):
        self._role = role

    def setRole(self, role):
        self._role = role

    @abstractmethod
    def execute(self):
        pass

class Left(GameCommand):
    """左移命令"""

    def execute(self):
        self._role.leftMove()
        self._role.showPosition()

class Right(GameCommand):
    """右移命令"""

    def execute(self):
        self._role.rightMove()
        self._role.showPosition()

class Up(GameCommand):
    """上移命令"""

    def execute(self):
        self._role.upMove()
        self._role.showPosition()

class Down(GameCommand):
    """下移命令"""

    def execute(self):
        self._role.downMove()
        self._role.showPosition()


class Jump(GameCommand):
    """跳躍命令"""

    def execute(self):
        self._role.jumpMove()
        self._role.showPosition()
        # 跳起後，空中停留半秒
        time.sleep(0.5)

class Squat(GameCommand):
    """蹲下命令"""

    def execute(self):
        self._role.squatMove()
        self._role.showPosition()
        # 蹲下後，伏地半秒
        time.sleep(0.5)


class Attack(GameCommand):
    """攻擊命令"""

    def execute(self):
        self._role.attack()

class MacroCommand(GameCommand):
    """巨集命令，也就是組合命令"""

    def __init__(self, role = None):
        super().__init__(role)
        self.__commands = []

    def addCommand(self, command):
        # 讓所有命令作用於同一個對象
        self.__commands.append(command)

    def removeCommand(self, command):
        self.__commands.remove(command)

    def execute(self):
        for command in self.__commands:
            command.execute()

class GameInvoker:
    """命令調度者"""

    def __init__(self):
        self.__command = None

    def setCommand(self, command):
        self.__command = command
        return self

    def action(self):
        if self.__command is not None:
            self.__command.execute()

if __name__ == "__main__":
    # 測試遊戲命令模式
    role = GameRole("Game Manager")
    invoker = GameInvoker()

    while True:
        strCmd = input("請輸入命令：");
        strCmd = strCmd.upper()
        if (strCmd == "L"):
            invoker.setCommand(Left(role)).action()
        elif (strCmd == "R"):
            invoker.setCommand(Right(role)).action()
        elif (strCmd == "U"):
            invoker.setCommand(Up(role)).action()
        elif (strCmd == "D"):
            invoker.setCommand(Down(role)).action()
        elif (strCmd == "JP"):
            cmd = MacroCommand()
            cmd.addCommand(Jump(role))
            cmd.addCommand(Squat(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "A"):
            invoker.setCommand(Attack(role)).action()
        elif (strCmd == "LU"):
            cmd = MacroCommand()
            cmd.addCommand(Left(role))
            cmd.addCommand(Up(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "LD"):
            cmd = MacroCommand()
            cmd.addCommand(Left(role))
            cmd.addCommand(Down(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "RU"):
            cmd = MacroCommand()
            cmd.addCommand(Right(role))
            cmd.addCommand(Up(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "RD"):
            cmd = MacroCommand()
            cmd.addCommand(Right(role))
            cmd.addCommand(Down(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "LA"):
            cmd = MacroCommand()
            cmd.addCommand(Left(role))
            cmd.addCommand(Attack(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "RA"):
            cmd = MacroCommand()
            cmd.addCommand(Right(role))
            cmd.addCommand(Attack(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "UA"):
            cmd = MacroCommand()
            cmd.addCommand(Up(role))
            cmd.addCommand(Attack(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "DA"):
            cmd = MacroCommand()
            cmd.addCommand(Down(role))
            cmd.addCommand(Attack(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "JA"):
            cmd = MacroCommand()
            cmd.addCommand(Jump(role))
            cmd.addCommand(Attack(role))
            cmd.addCommand(Squat(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "Q"):
            exit()