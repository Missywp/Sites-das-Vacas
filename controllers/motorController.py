from flask import Blueprint, request, render_template, redirect, url_for
from utils.decorators import role_required
motor = Blueprint("motor_blueprint", __name__, template_folder="templates")

@motor.route('/motores')
@role_required(roles=['admin', 'veterinario','funcionario'])
def motores():
    return render_template("motor.html")

@motor.route('/cadastrarMotor')
@role_required(roles=['admin'])
def cadastrarMotor():
    return render_template('cadastrarMotor.html')

@motor.route("editarMotor")
@role_required(roles=['admin'])
def editarMotor():
    return render_template("editarMotor.html")
