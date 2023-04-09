from src.dbs.database import banco

class PlanoModel(banco.Model):
    __tablename__: 'planos'
    
    id_plano = banco.Column(banco.Integer, primary_key=True, autoincrement=True)
    nome = banco.Column(banco.String(200))
    cobertura = banco.Column(banco.String(100))
    operadora_id = banco.Column(banco.Integer)
    
    

def __init__(self, nome, cobertura, operadora_id):
    
    self.nome = nome
    self.cobertura = cobertura
    self.operadora_id = operadora_id 
    
    
def json(self):
    return {
        
        'nome' : self.nome,
        'cobertura' : self.cobertura,
        'operadora_id' : self.operadora_id
    }