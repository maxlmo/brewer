import os
from flask import Flask, render_template
from flask_injector import FlaskInjector
from injector import inject

from src.dependency_injection import configure
from src.sensor.temperature_sensor import TemperatureSensor

app: Flask = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)
app._static_folder = os.path.abspath("templates/static/")


@app.route('/')
def index():
    return render_template("index.html")


@inject
@app.route('/temp')
def get_temperature(ts: TemperatureSensor) -> str:
    return str(ts.read_temperature())


FlaskInjector(app=app, modules=[configure])
app.run('0.0.0.0')
