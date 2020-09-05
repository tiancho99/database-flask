from .models import db, Personas, Locaciones

def intert_persona(id, nombre, apellido, locacion):
    persona = Personas(id, nombre, apellido, locacion)
    db.session.add(persona)
    db.session.commit()

def delete_persona(id):
    persona = Personas.query.filter_by(id=id).first()
    db.session.delete(persona)
    db.session.commit()

def get_personas():
    persona = Personas.query.all()
    return persona

def get_persona(id):
    persona = Personas.query.filter_by(id=id).first()
    return persona