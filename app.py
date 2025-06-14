from flask import Flask, render_template, request
from controllers.app_controller import create_app
from controllers.usersController import user
from controllers.configAmbienteController import configAmbientes
from controllers.dadosAtuaisController import dadosAtuais
from controllers.historicoController import historico
from controllers.balancaController import balanca
from controllers.motorController import motor

if __name__ == '__main__':
    app = create_app()
    app.register_blueprint(user, url_prefix='/')
    app.register_blueprint(configAmbientes, url_prefix='/')
    app.register_blueprint(dadosAtuais, url_prefix='/')
    app.register_blueprint(historico, url_prefix='/')
    app.register_blueprint(balanca, url_prefix='/')
    app.register_blueprint(motor, url_prefix='/')
    
    app.run(host='0.0.0.0', port=8080, debug=True)