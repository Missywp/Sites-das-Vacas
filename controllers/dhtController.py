from flask import Blueprint, request, render_template, redirect, url_for
from utils.decorators import role_required

dht = Blueprint("dht_blueprint", __name__, template_folder="templates")

@dht.route("/dhts")
@role_required(roles=['admin', 'veterinario', 'funcionario'])
def dhts():
    return render_template("dht.html")

@dht.route('/cadastrarDht')
@role_required(roles=['admin'])
def cadastrarDht():
    return render_template('cadastrarDHT.html')

@dht.route("/edtiarDht")
@role_required(roles=['admin'])
def editarDht():
    return render_template("editarDht.html")
