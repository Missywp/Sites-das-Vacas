from flask import Blueprint, request, render_template, redirect, url_for

motor = Blueprint("motor_blueprint", __name__, template_folder="templates")

@motor.route('/cadastrarMotor')
def cadastrarMotor():
    return render_template('cadastrarMotor.html')

@motor.route('/motores')
def motores():
    return render_template("motor.html")
