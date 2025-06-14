from flask import Blueprint, request, render_template, redirect, url_for

motor = Blueprint("motor_blueprint", __name__, template_folder="templates")

@motor.royte('/cadastrarMotor')
def cadastrarMotor():
    return render_template('cadastrarMotor.html')
