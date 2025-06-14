from flask import Blueprint, request, render_template, redirect, url_for

dht = Blueprint("dht_blueprint", __name__, template_folder="templates")

@dht.route('/cadastrarDht')
def cadastrarDht():
    return render_template('cadastrarDHT.html')

@dht.route("/dhts")
def dhts():
    return render_template("dht.html")