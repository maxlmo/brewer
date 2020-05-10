import time, sys

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.led_matrix.device import max7219
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from luma.core.virtual import viewport

from temperatureSensor import TemperatureSensor
    
sensorPath = "/sys/bus/w1/devices/28-0119136e048d/w1_slave"
tempSensor = TemperatureSensor(sensorPath)

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=32, height=8, block_orientation=-90)

try:
    while True:
        tempstr = str(tempSensor.getCurrentTemperature()) + " °C"
        print(time.strftime('%H:%M:%S') +  " temp: " + tempstr)
        time.sleep(1)
        
        with canvas(device) as draw:
            text(draw, (1, 1), tempstr, fill="white", font=proportional(CP437_FONT))

except KeyboardInterrupt:
    print("key interrupt")
except Exception as e:
    print(str(e))
    sys.exit(1)
finally:
    print("exit")
    sys.exit(0)
    
