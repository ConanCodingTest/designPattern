"""Mediator Pattern Example: Device Manager"""

from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法
from enum import Enum

class DeviceType(Enum):
    """設備類型枚舉"""
    TypeSpeaker = 1
    TypeMicrophone = 2
    TypeCamera = 3

class DeviceItem:
    """設備項目類別"""
    def __init__(self, id, name, type, isDefault=False):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__isDefault = isDefault

    def __str__(self):
            return "type:" + str(self.__type) + " id:" + str(self.__id) + " name:" + str(self.__name) + " isDefault:" + str(self.__isDefault)

    def getId(self):
            return self.__id

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def isDefault(self):
        return self.__isDefault
    
class DeviceList:
    """設備列表類別"""
    def __init__(self):
        self.__devices = []

    def add(self, deviceItem):
        """添加設備"""
        self.__devices.append(deviceItem)

    def getCount(self):
        return len(self.__devices)

    def getByIdx(self, idx):
        if idx < 0 or idx >= self.getCount():
            return None
        return self.__devices[idx]

    def getById(self, id):
        for item in self.__devices:
            if( item.getId() == id):
                return item
        return None

class DeviceMgr(metaclass=ABCMeta):
    """設備管理器抽象類別"""
    @abstractmethod
    def enumerate(self):
        """列舉設備，初始化需要重新獲得設備清單"""
        pass

    @abstractmethod
    def active(self, deviceId):
        """獲取使用設備"""
        pass

    @abstractmethod
    def getCurDeviceId(self):
        """獲取當前設備ID"""
        pass

class SpeakerMgr(DeviceMgr):
    """揚聲器管理器類別"""
    def __init__(self):
        self.__curDeviceId = None

    def enumerate(self):
        """列舉揚聲器設備"""
        # 模擬獲取設備
        devices = DeviceList()
        devices.add(DeviceItem("369dd760-893b-4fe0-89b1-671eca0f0224", "Realtek High Definition Audio", DeviceType.TypeSpeaker))
        devices.add(DeviceItem("59357639-6a43-4b79-8184-f79aed9a0dfc", "NVIDIA High Definition Audio", DeviceType.TypeSpeaker, True))
        return devices

    def active(self, deviceId):
        """激活指定ID的揚聲器設備"""
        self.__curDeviceId = deviceId

    def getCurDeviceId(self):
        """獲取當前揚聲器設備ID"""
        return self.__curDeviceId
    
class DeviceUtil:
    """設備工具類別"""
    def __init__(self):
        self.__mgrs = {}
        self.__mgrs[DeviceType.TypeSpeaker] = SpeakerMgr()
        # 節省篇幅，MicrophoneMgr和CameraMgr不再實現
        # self.__microphoneMgr = MicrophoneMgr()
        # self.__cameraMgr = CameraMgr

    def __getDeviceMgr(self, type):
        return self.__mgrs[type]

    def getDeviceList(self, type):
        return self.__getDeviceMgr(type).enumerate()

    def active(self, type, deviceId):
        self.__getDeviceMgr(type).active(deviceId)

    def getCurDeviceId(self, type):
        return self.__getDeviceMgr(type).getCurDeviceId()
    
if __name__ == "__main__":
    deviceUtil = DeviceUtil()
    deviceList = deviceUtil.getDeviceList(DeviceType.TypeSpeaker)
    print("揚聲器設備列表:")
    if deviceList.getCount() > 0:
        # 設置默認揚聲器設備
        deviceUtil.active(DeviceType.TypeSpeaker, deviceList.getByIdx(0).getId())
    for idx in range(deviceList.getCount()):
        device = deviceList.getByIdx(idx)
        print(device)

    # 激活一個揚聲器設備
    print("當前揚聲器設備:" + deviceList.getById(deviceUtil.getCurDeviceId(DeviceType.TypeSpeaker)).getName())
