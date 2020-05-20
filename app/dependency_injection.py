from flask_injector import request
from injector import singleton


from .config import use_fake
from .display.fake_led_display import FakeLedDisplay
from .display.led_display import LedDisplay
from .sensor.fake_temperature_sensor import FakeTemperatureSensor
from .sensor.temperature_sensor import TemperatureSensor


def configure(binder):
    if use_fake:
        binder.bind(TemperatureSensor, to=FakeTemperatureSensor, scope=request)
        binder.bind(LedDisplay, to=FakeLedDisplay, scope=singleton)
    else:
        binder.bind(LedDisplay, to=LedDisplay, scope=singleton)
        binder.bind(TemperatureSensor, to=TemperatureSensor, scope=request)

