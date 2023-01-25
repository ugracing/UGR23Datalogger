#Will contain the parent class for sensors


class Sensor:
    def __init__(self, CANID, Name, Bytes, Dist, Inst):
        self.CANID = CANID
        self.name = Name
        self.bytes = Bytes
        self.dist = Dist
        self.inst = Inst
        self.data = []

    def distData(self):
        distTotal = 0
        distList = []
        for i in range(len(self.dist)):
            distTotal += int(i)
            distList.append(int(i))

        distSection = distTotal/distList[0]


        chunks = [self.rawData[j:j+n] for j in range(int(self.bytes))]

        

