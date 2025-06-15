from flask import Blueprint, request, render_template, redirect, url_for
from utils.decorators import role_required

balanca = Blueprint("balanca_blueprint", __name__, template_folder="templates")

@balanca.route('/balancas')
@role_required(roles=['admin', 'funcionario', 'veterinario'])
def balancas():
    return render_template('balanca.html')

@balanca.route('/cadastrarBalanca')
@role_required(roles=['admin'])
def cadastrarBalanca():
    return render_template('cadastrarBalanca.html')

@balanca.route('/editarBalanca')
@role_required(roles=['admin'])
def editarBalanca():
    return render_template('editarBalanca.html')
