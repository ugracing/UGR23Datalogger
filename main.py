#will contain the main function that will run

import Sensor

if __name__ == "__main__":
    testSensor = Sensor.Sensor("0000","Test","8","2222","Test Sensor")

    testData = "0000111122223333"

    print(testSensor.distributeData(testData))