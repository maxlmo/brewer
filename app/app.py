import os
from flask import Flask, render_template, jsonify
from flask_injector import FlaskInjector
from injector import inject
from flask import request
import threading
import atexit
import time

from app.dependency_injection import configure
from app.display import get_display
from app.sensor import get_temperature_sensor
from app.sensor.fake_temperature_sensor import FakeTemperatureSensor
from app.sensor.temperature_sensor import TemperatureSensor

min = 50
max = 100


POOL_TIME = 2

# variables that are accessible from anywhere
current_temperature = 0
# lock to control access to variable
dataLock = threading.Lock()
# thread handler
thread = threading.Thread()


def create_app():
    app: Flask = Flask(__name__)
    app.config.update(TEMPLATES_AUTO_RELOAD=True)
    app._static_folder = os.path.abspath("app/templates/static/")

    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route('/range', methods=['POST'])
    def set_range_value():
        global min, max
        min = request.get_json()["min"]
        max = request.get_json()["max"]
        return ""

    @app.route('/range', methods=['GET'])
    def send_range_value():
        return jsonify({"min": min, "max": max})

    @app.route("/temp")
    def temp():
        global current_temperature
        return str(round(current_temperature, 0))

    def stop_thread():
        global thread
        thread.cancel()

    def loop():
        global current_temperature
        temp_sensor = get_temperature_sensor()
        display = get_display()
        while True:
            current_temperature = temp_sensor.read_temperature()
            display.display_text(str(current_temperature))
            print(current_temperature)
            time.sleep(POOL_TIME)

    def start_threat():
        # Do initialisation stuff here
        global thread
        # Create your thread
        thread = threading.Timer(POOL_TIME, loop, ())
        thread.start()

    start_threat()
    FlaskInjector(app=app, modules=[configure])
    atexit.register(stop_thread)
    return app
