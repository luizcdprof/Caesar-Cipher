from flask import Flask, render_template

def create_app():
    #Create and configure the app
    app = Flask(__name__)

    @app.route("/")
    def home(name='Home'):
        return render_template('index.html', name=name)

    @app.route("/encode")
    def encode(name='Encode'):
        return render_template('encode.html', name=name)
    
    return app
