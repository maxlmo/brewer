import os
from flask import Flask, render_template, jsonify
from flask_injector import FlaskInjector
from injector import inject
from flask import request

from src.dependency_injection import configure
from src.sensor.temperature_sensor import TemperatureSensor

app: Flask = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)
app._static_folder = os.path.abspath("templates/static/")

min = 50
max = 100

@app.route('/')
def index():
    return render_template("index.html")


@inject
@app.route('/temp')
def get_temperature(ts: TemperatureSensor) -> str:
    return str(ts.read_temperature())


@app.route('/range', methods=['POST'])
def set_range_value():
    global min, max
    min = request.get_json()["min"]
    max = request.get_json()["max"]
    return ""


@app.route('/range', methods=['GET'])
def send_range_value():
    return jsonify({"min": min, "max": max})


FlaskInjector(app=app, modules=[configure])
app.run('0.0.0.0')
