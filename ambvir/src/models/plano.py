from src.dbs.database import banco

def __init__(self, id_plano, nome, cobertura, operadora_id):
    self.id_plano = id_plano
    self.nome = nome
    self.cobertura = cobertura
    self.operadora_id = operadora_id 
    
    
def json(self):
    return {
        'id_plano' = self.id_plano,
        'nome' = self.nome,
        'cobertura' = self.cobertura,
        'operadora_id' = self.operadora_id
    }