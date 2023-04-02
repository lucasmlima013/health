from src.dbs.database import banco

class AtendimentossModel(banco.Model):
    __tablename__ = 'atendimentos'

    id_atendimento = banco.Colum(banco.Integer, PrimaryKey = True)
    data = banco.Column(banco.Datetime)
    pessoa_id = banco.Column(banco.Integer)
    especialidade = banco.Column(banco.Integer)
    plantao = banco.Column(banco.Boolean)
    tipo = banco.Column(banco.tipo)
    
def __init__(self, id_atendimento, data, pessoa_id, especialidade, plantao, tipo):
    self.id_atendimento = id_atendimento
    self.data = data
    self.pessoa_id = pessoa_id
    self.especialidade = especialidade
    self.plantao = plantao
    self.tipo = tipo

def json(self):
        return {
            'id_atendimento': self.id_atendimento,
            'data': self.data,
            'pessoa_id': self.pessoa_id,
            'especialidade': self.especialidade,
            'plantao': self.plantao,
            'tipo' : self.tipo
        }
        
        
