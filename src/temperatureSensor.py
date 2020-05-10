class TemperatureSensor:

    def __init__(self, path):
        self.path = path 

    def getCurrentTemperature(self):
        file = open(self.path, 'r')
        lines = file.readlines()
        file.close()
        temperaturStr = lines[1].find('t=')
        tempData = lines[1][temperaturStr+2:]
        tempCelsius = float(tempData) / 1000.0
        return tempCelsius