"""Login error Observer Pattern Implementation"""

import time #導入時間處理模塊
from observer import Observer, Observable

class Account(Observable):
    """使用者帳號類別，繼承自 Observable"""

    def __init__(self):
        super().__init__()
        self.__latestIp = {}
        self.__latestRegion = {}

    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        if self.__isLongDistance(name, region):
            self.notifyObservers({"name": name, "ip": ip, "region": region, "time": time})
        self.__latestRegion[name] = region
        self.__latestIp[name] = ip

    def __getRegion(self, ip):
        # 由IP Address獲取地區資訊，模擬
        ipRegions = {
            "101.47.18.9": "台灣台北",
            "67.218.147.69":"美國洛杉磯"
        }
        region = ipRegions.get(ip)
        return "" if region is None else region


    def __isLongDistance(self, name, region):
        # 計算本次登陸與最近幾次登陸的區域差距。
        # 用此串匹配來類比，實際需用地理資訊相關服務
        latestRegion = self.__latestRegion.get(name)
        return latestRegion is not None and latestRegion != region;


class SmsSender(Observer):
    """訊息發送器"""

    def update(self, observable, object):
        print("[訊息發送] " + object["name"] + "您好!檢測到您的帳戶可能登陸異常。最近一次登錄資訊：\n"
            + "登錄地區：" + object["region"] + "  登錄ip：" + object["ip"] + "  登錄時間："
            + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


class MailSender(Observer):
    """Mail發送器"""

    def update(self, observable, object):
        print("[Mail發送] " + object["name"] + "您好!檢測到您的帳戶可能登陸異常。最近一次登錄資訊：\n"
            + "登錄地區：" + object["region"] + "  登錄ip：" + object["ip"] + "  登錄時間："
            + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))
        
if __name__ == "__main__":
    # 測試程式
    account = Account()
    sms_sender = SmsSender()
    mail_sender = MailSender()

    account.addObserver(sms_sender)
    account.addObserver(mail_sender)

    # 模擬登錄行為
    account.login("Tony", "101.47.18.9", time.time())
    account.login("Tony", "67.218.147.69", time.time())