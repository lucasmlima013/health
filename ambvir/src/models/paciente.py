from src.dbs.database import banco


class PessoasModel(banco.Model):
    __tablename__ = 'pessoas'
    id_pessoa = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(100))
    data_nascimento = banco.Column(banco.Date)
    plano = banco.Column(banco.Integer)
    numero_plano = banco.Column(banco.Integer)
    

def __init__(self, id_pessoa, nome, data_nascimento, plano, numero_plano):
    self.id_pessoa = id_pessoa
    self.nome = nome
    self.data_nascimento = data_nascimento
    self.plano = plano
    self.numero_plano = numero_plano
    

    