from flask_injector import request
from injector import singleton


from src.config import use_fake
from src.display.fake_led_display import FakeLedDisplay
from src.display.led_display import LedDisplay
from src.sensor.fake_temperature_sensor import FakeTemperatureSensor
from src.sensor.temperature_sensor import TemperatureSensor


def configure(binder):
    if use_fake:
        binder.bind(TemperatureSensor, to=FakeTemperatureSensor, scope=request)
        binder.bind(LedDisplay, to=FakeLedDisplay, scope=singleton)
    else:
        binder.bind(LedDisplay, to=LedDisplay, scope=singleton)
        binder.bind(TemperatureSensor, to=TemperatureSensor, scope=request)

