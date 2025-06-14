from flask import Blueprint, request, render_template, redirect, url_for

balanca = Blueprint("balanca_blueprint", __name__, template_folder="templates")

@balanca.route('/cadastrarBalanca')
def cadastrarBalanca():
    return render_template('cadastrarBalanca.html')

@balanca.route('/balancas')
def balancas():
    return render_template('balanca.html')