from flask import Blueprint, request, render_template, redirect, url_for

atuador = Blueprint("atuador_blueprint", __name__, template_folder="templates")

@atuador.rote('/cadastrarAtuador')
def cadastrarAtuador():
    return render_template('cadastrarAtuador.html')