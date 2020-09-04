from flask import Markup

from app import create_app

app = create_app()

@app.route('/')
def main():
    return Markup('<p>hola mundo</p>')