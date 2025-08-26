# backend/app.py

from flask import Flask

# Se crea una instancia de la aplicación Flask
app = Flask(__name__)

# Se define una ruta básica de prueba
@app.route('/api/test')
def hello_world():
    # Esta ruta devolverá un simple mensaje en formato JSON
    return {'message': 'Hola, Mundo desde Flask!'}

# Esto es para asegurar que el servidor solo se ejecute cuando el script es ejecutado directamente
if __name__ == '__main__':
    app.run(debug=True)