from flask import Flask, render_template, request, flash
from app.encode import encode_message

def create_app():
    #Create and configure the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asbvjadbfvskhjdhfkjsdgsdgb'

    @app.route('/')
    def home(name='Home'):
        return render_template('index.html', name=name)

    @app.route('/encode', methods=('GET', 'POST'))
    def encode(name='Encode'):
        if request.method == 'POST':
            try:
                cipher_key = int(request.form['cipher_key'])
            except:
                cipher_key = 0
            
            message = request.form['message']

            if cipher_key == 0:
                flash("A chave deve ser um número!")
            elif not cipher_key:
                flash('A chave é obrigatória...')
            elif not message :
                flash('A mensagem é necessária...')
            else:
                encoded_message = encode_message(message, int(cipher_key))
                flash(encoded_message)

        return render_template('encode.html',name=name)
    
    return app
