"""Water Heater Observer Pattern Implementation"""

from observer import Observer, Observable

class WaterHeater(Observable):
    """熱水器類別，繼承自 Observable"""

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("目前溫度是：" + str(self.__temperature) + "℃")
        self.notifyObservers()


class WashingMode(Observer):
    """洗澡模式"""

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) \
                and observable.getTemperature() >= 50 and observable.getTemperature() < 70:
            print("水已燒好!溫度正好可以用來洗澡。")


class DrinkingMode(Observer):
    """飲用模式"""

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("水已燒開！可以飲用了。")

if __name__ == "__main__":
    # 測試程式
    water_heater = WaterHeater()
    washing_mode = WashingMode()
    drinking_mode = DrinkingMode()

    water_heater.addObserver(washing_mode)
    water_heater.addObserver(drinking_mode)

    # 設定溫度並通知觀察者
    water_heater.setTemperature(30)
    water_heater.setTemperature(50)
    water_heater.setTemperature(100)
    water_heater.setTemperature(70)