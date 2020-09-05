from flask import Markup

from app import create_app
from app.mysql_service import get_personas, get_persona, intert_persona, delete_persona

app = create_app()

@app.route('/')
def main():
    intert_persona(1,'sebastian','hernandez', None)
    delete_persona(1)
    persona = get_persona(2)
    personas = get_personas()
    # delete_persona(1)
    return Markup('<p>hola {}</p>'.format('borrado exitoso'))