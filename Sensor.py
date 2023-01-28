#Will contain the parent class for sensors

class Sensor:
    # Constructor of the class Sensor
    def __init__(self, CANID, Name, Bytes, Dist, Inst):
        self.CANID = CANID
        self.name = Name
        self.bytes = Bytes
        self.dist = Dist
        self.inst = Inst
        self.data = []

    #Seperate the data into it distribution attributes  
    def distributeData(self,data):
        dataBytes = []
        distData = []
        for i in range(len(self.bytes)):
            dataBytes.append(list(data[i*4:(i+1)*4]))
        
        for d in range(len(self.dist)):
            thisDist = []
            for i in range(int(self.dist[d])):
                thisDist.append(dataBytes.pop(i))
                print(dataBytes)
            distData.append(thisDist)
        return distData

            



        

