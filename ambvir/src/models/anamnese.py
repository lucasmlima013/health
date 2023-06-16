from src.dbs.database import banco

class AnamneseModel(banco.Model):
    __tablename__ = 'anamnese'

    id_anamnese = banco.Colum(banco.Integer, PrimaryKey = True)
    data = banco.Column(banco.Datetime)
    questao_id = banco.Column(banco.Integer)
   
def __init__(self, id_anamnese, data, questao_id):
    self.id_anamnese = id_anamnese
    self.data = data
    self.questao_id = questao_id

def json(self):
        return {
            'id_anamnese': self.id_anamnese,
            'data': self.data,
            'questao_id': self.pessoa_id
        }
          
