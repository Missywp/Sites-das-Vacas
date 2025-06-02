from flask import Flask, render_template, request
from controllers.app_controller import create_app
from users import user
from configAmbiente import configAmbientes

if __name__ == '__main__':
    app = create_app()
    app.register_blueprint(user, url_prefix='/')
    app.register_blueprint(configAmbientes, url_prefix='/')
    app.run(host='0.0.0.0', port=8080, debug=True)