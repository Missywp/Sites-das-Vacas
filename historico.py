from flask import Blueprint, request, render_template, redirect, url_for

historico = Blueprint("historico_blueprint", __name__, template_folder="templates")