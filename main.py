# # 21
class Yozuvchi:
    def __init__(self, ism):
        self.ism = ism

    def yozish(self):
        print("Yozmoqda")

class Shoir(Yozuvchi):
    def yozish(self):
        print("She’r yozmoqda")

a = Shoir("Alisher")
a.yozish()


# # 22
class Internet:
    def __init__(self, tezlik):
        self.tezlik = tezlik

    def ulanish(self):
        print("Ulandi")

class WiFi(Internet):
    def ulanish(self):
        print("WiFi ulandi")

a1 = Internet(100)
a2 = WiFi(50)

a1.ulanish()
a2.ulanish()

