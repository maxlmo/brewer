class TemperatureSensor:

    def __init__(self, path):
        self.path = path 

    def readTemperature(self):
        f = open(sensorName, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def readTempLines(self):
        lines = self.readTempSensor(self.path)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = readTempSensor(sensorName)
        temperaturStr = lines[1].find('t=')
        if temperaturStr != -1:
            tempData = lines[1][temperaturStr+2:]
            tempCelsius = float(tempData) / 1000.0
            tempKelvin = 273 + float(tempData) / 1000
            tempFahrenheit = float(tempData) / 1000 * 9.0 / 5.0 + 32.0
            return [tempCelsius, tempKelvin, tempFahrenheit]
