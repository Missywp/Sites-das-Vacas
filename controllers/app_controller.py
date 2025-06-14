from flask import Flask, render_template, request

def create_app():
    app = Flask( __name__,
    template_folder="./templates/",
    static_folder="./static/",
    root_path="./")
    
    app.secret_key = 'chave-secreta'
    
    @app.route('/')
    def index():
        return render_template("login.html")
    return app
