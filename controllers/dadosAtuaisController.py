from flask import Blueprint, request, render_template, redirect, url_for

dadosAtuais = Blueprint("dadosAtuais_blueprint", __name__, template_folder="templates")

@dadosAtuais.route('/dadoAtual')
def dadoAtual():
    return render_template('dadosAtuais.html')