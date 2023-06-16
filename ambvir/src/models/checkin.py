from src.dbs.database import banco

class CheckinModel(banco.Model):
    __tablename__ = 'checkin'

    id_checkin = banco.Colum(banco.Integer, PrimaryKey = True)
    data = banco.Column(banco.Datetime)
    
def __init__(self, id_checkin, data):
    self.id_checkin = id_checkin
    self.data = data


def json(self):
        return {
            'id_checkin': self.id_checkin,
            'data': self.data
        }