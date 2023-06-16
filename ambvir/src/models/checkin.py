from src.dbs.database import banco

class CheckinModel(banco.Model):
    __tablename__ = 'checkin'

    id_checkin = banco.Colum(banco.Integer, PrimaryKey = True)
    data = banco.Column(banco.Datetime)
