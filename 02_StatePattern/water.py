"""Water state module."""

from state import Context, State

class WaterState(Context):
    """水的狀態類別，繼承自 Context"""

    def __init__(self):
        super().__init__()
        self.addState(SolidState("Solid"))
        self.addState(LiquidState("Liquid"))
        self.addState(GasState("Gas"))
        self.setTemperature(25) # 初始溫度

    def getTemperature(self):
        """獲取當前溫度"""
        return self._getStateInfo()
    
    def setTemperature(self, temperature):
        """設定溫度並改變狀態"""
        self._setStateInfo(temperature)

    def riseTemperature(self, step):
        """升高溫度"""
        self.setTemperature(self.getTemperature() + step)

    def reduceTemperature(self, step):
        """降低溫度"""
        self.setTemperature(self.getTemperature() - step)

    def behavior(self):
        """執行當前狀態的行為"""
        state = self.getState()
        if isinstance(state, State):
            state.behavior(self)

# 單例的裝飾器
def singleton(cls, *args, **kwargs):
    """單例模式裝飾器"""
    instances = {}
    def get_instance(*args, **kwargs):
        """獲取單例實例"""
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class SolidState(State):
    """固態水"""
    
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo < 0

    def behavior(self, context):
        print("當前溫度", context._getStateInfo(), "℃，水處於固態，冰冷的感覺。")

@singleton
class LiquidState(State):
    """液態水"""
    
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return 0 <= stateInfo < 100

    def behavior(self, context):
        print("當前溫度", context._getStateInfo(), "℃，水處於液態，可以飲用。")

@singleton
class GasState(State):
    """氣態水"""
    
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo >= 100

    def behavior(self, context):
        print("當前溫度", context._getStateInfo(), "℃，水處於氣態，蒸汽升騰。")

if __name__ == "__main__":
    # 測試程式
    water = WaterState()
    # 初始狀態
    water.behavior()
    
    # 改變溫度並檢查狀態
    water.setTemperature(-4)  # -4℃
    water.behavior()
    
    water.riseTemperature(18)  # 14℃
    water.behavior()
    
    water.riseTemperature(86)  # 100℃
    water.behavior()
