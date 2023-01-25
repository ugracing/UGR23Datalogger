#will contain the input function for the csv fle

class DataReader:

  # Constructor with specified sensors
	def __init__(self, fileName, sensors, sensorList, path):
		self.fileName = fileName #name of file to read
		self.sensors = sensors #list of sensors
		self.sensorList = sensorList #list of recognised sensors
		self.path = path #path to data files
		# note - update with a list of accepted canIDs and sensors.
		for s in sensors:
			if s not in sensorList: 
				self.SensorNotFound(sensor = s)
				print("Sensor not found, it will not be checked for")
				continue

  # Constructor with unspecified sensors - read all of them
	def __init__(self, fileName, path):
		self.fileName = fileName #name of file to read
		self.path = path #path to data files

	# custom exception for SensorNotFound
	def SensorNotFound(Exception, sensor):
		print("The sensor " + sensor + "requested has not been initialised, please make sure it is in the config file")
		pass
		
	# Function to read the file
	def readFile(self, sensors):
		try:
			file = open(self.path + "/" + self.fileName, "r")
		except:
			raise FileNotFoundError()


		checkSensor = True
		#check if there's specified sensors
		if (sensors.isEmpty()):
			checkSensor = False # False -> none specified
		
		for line in file:
			line = line[:-1] #remove \n from the end of each line
			
			dataPoints = line.split(",")
			#[0] is time, [1] is the canID, [2] is the data.
			
			if len(line) <= 42 and len(dataPoints) == 3 : #check if line is broken

				if (not checkSensor): #if we're not looking for certain sensors
					
					if dataPoints[1] not in self.sensorList: 
						self.SensorNotFound(sensor = dataPoints[1])
						continue
						
					sensor = self.sensorList[dataPoints[1]]
					sensor.addTime([dataPoints[0]]) #implemented in Sensor
					sensor.addReading([dataPoints[2]]) #implemented in Sensor
		
				else: #if we are looking for certain sensors
					sensor = self.sensorList[dataPoints[1]]
					sensor.addTime([dataPoints[0]]) #implemented in Sensor
					sensor.addReading([dataPoints[2]]) #implemented in Sensor
					
		


			