from flask import Flask

def create_app():
    #Create and configure the app
    app = Flask(__name__)

    #A simple page that says Hello
    @app.route('/hello')
    def hello():
        return 'Hello World!'
    
    return app
