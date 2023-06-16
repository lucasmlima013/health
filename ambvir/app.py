from flask import Flask
from flask_restful import Api
from src.dbs.database import banco, app

api = Api(app)

@app.route('/')
def index():
    return 'Bem vindo a API!!!'


@app.before_first_request
def cria_banco():
    banco.create_all()
    
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == "__main__":
    app.run(debug=True)