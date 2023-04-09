from src.dbs.database import banco
from flask_restful import Resource, reqparse
from src.models.atendimento import AtendimentosModel


class Atendimentos(Resource):
    def get(self):
        return {'atedimentos': Atendimentos}


class Atendimento(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('data')
    atributos.add_argument('pessoa_id')
    atributos.add_argument('especialidade')
    atributos.add_argument('plantao')
    atributos.add_argument('tipo')

    def find_atendimento(atendimento_id):
        for pessoa in Atendimento:
            if ['atendimento_id'] == atendimento_id:
                return Atendimento
        return False