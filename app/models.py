from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Personas(db.Model):
    __tablename__ = 'personas'
    def __init__(self, id, nombre, apellido, locacion):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.id_locacion = locacion

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=True)
    id_locacion = db.Column(db.Integer, db.ForeignKey('locaciones.id'))

class Locaciones(db.Model):
    __tablename__ = 'locaciones'
    def __init__(self, id, ciudad, estado):
        self.id = id
        self.ciudad = ciudad
        self.estado = estado

    id = db.Column(db.Integer, primary_key=True)
    ciudad = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(100), nullable=False)
    persona = db.relationship('Personas', backref='persona', lazy=True)