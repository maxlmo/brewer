import time, sys
from temperatureSensor import TemperatureSensor
    
sensorPath = "/sys/bus/w1/devices/28-0119136e048d/w1_slave"
tempSensor = TemperatureSensor(sensorPath)

try:
    while True:
        print(time.strftime('%H:%M:%S')  " temp: " + str(tempSensor.readTempLines()[0]) + " °C")
        time.sleep(1)
except KeyboardInterrupt:
    print("key interrupt")
except Exception as e:
    print(str(e))
    sys.exit(1)
finally:
    print("exit")
    sys.exit(0)