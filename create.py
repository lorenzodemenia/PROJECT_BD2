from app import *


class Utenti(db.Model):
    __tablename__='utenti'

    id_users=db.Column(db.VARCHAR(50),primary_key=True)
    name=db.Column(db.VARCHAR(50))
    surname=db.Column(db.VARCHAR(50))
    mail=db.Column(db.VARCHAR(50))
    data_n=db.Column(db.Date)

    def __init__(self, id_users, name, surname, mail, data_n):
        self.id_users=id_users
        self.name=name
        self.surname=surname
        self.mail=mail
        self.data_n=data_n


