from flask import Blueprint, request, render_template, redirect, url_for

user = Blueprint("user_blueprint", __name__, template_folder="templates")

users = {
    'user1': '1234',
    'user2': '1234'
}

@user.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        print(user, password)
        if user in users and users[user] == password:
            minha_casa = {'Quarto': '/quarto', 'Banheiro': '/banheiro'}
            return render_template('base.html')
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('login.html')