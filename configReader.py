import csv
import Sensor

class ConfigReader:
    def __init__(self, file):
        self.file = file
        self.sensors = []
        self.sensorObjs = []

    def readFile(self):
        with open(self.file) as file:
            reader = csv.reader(file, delimiter=',')
            lineCount = 0
            for line in reader:
                if lineCount == 0:
                    fileKeys = list(line)
                    #print(fileKeys)
                else:
                    #Dict representation of sensor 
                    temp = {}
                    for i in  range(len(line[1:])):
                        #print(fileKeys[i+1], line[i+1])
                        temp[fileKeys[i+1]] = line[i+1]
                    self.sensors.append({line[0]:temp})

                    #Adding Object representation of Sensor
                    newSensor = Sensor(line[0],line[1],line[2],line[3],line[4],line[5])
                    self.sensorObjs.append(newSensor)
                lineCount += 1
        return self.sensors

CSVReader = ConfigReader("CONFIG.CSV")
print(CSVReader.readFile())