from flask import Blueprint, request, render_template, redirect, url_for

sensor = Blueprint("sensor_blueprint", __name__, template_folder="templates")

@sensor.rote('/cadastrarSensor')
def cadastrarSensor():
    return render_template('cadastrarSensor.html')