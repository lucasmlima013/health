from flask import Flask, jsonify, request
from flask_restful import Api
from flask_cors import CORS, cross_origin
from src.dbs.database import banco, app

api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/atendimento', methods=['POST', 'OPTIONS'])
def post_sentimentopessoa():
    if request.method == 'OPTIONS':
        return jsonify(''), 200
    dados = request.get_json()
    sentimentopessoa = SentimentoPessoa()
    sentimentopessoa.salvar_sentimentopessoa(dados)
    return jsonify(''), 201


if __name__ == '__main__':
    app.run(debug=True)