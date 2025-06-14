from flask import Blueprint, request, render_template, redirect, url_for

configAmbientes = Blueprint("configAmbiente_blueprint", __name__, template_folder="templates")

@configAmbientes.route('/configAmbiente')
def configAmbiente():
    return render_template('configAmbiente.html')