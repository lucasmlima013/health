from flask import Flask
from flask_restful import Api
from src.dbs.database import banco

app = Api(app)

@app.route('/')
def index():
    return 'Bem vindo a API!!!'


@app.before_first_request
def cria_banco():
    banco.create_all()

if __name__ == "__main__":
    app.run(debug=True)