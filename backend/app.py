# backend/app.py
import os
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask

# --- INICIALIZACIÓN ---
# Busca la llave que descargaste
cred = credentials.Certificate("credentials.json") 
firebase_admin.initialize_app(cred)

# Conéctate a la base de datos de Firestore
db = firestore.client()
print("✅ Conectado a Firebase")

# Inicializa la aplicación de Flask
app = Flask(__name__)

# --- RUTAS DE EJEMPLO ---
@app.route('/')
def hello_world():
    return '¡Hola, mundo! ¡El backend de LimpiaGest está funcionando!'

# --- PRUEBA DE CONEXIÓN A LA BASE DE DATOS ---
@app.route('/test-db')
def test_db():
    try:
        # Intenta leer una colección (aunque no exista)
        users_ref = db.collection('users').limit(1).get()
        return "✅ ¡Conexión con Firestore exitosa!"
    except Exception as e:
        return f"❌ Error conectando a Firestore: {e}"

# Para ejecutar la app (opcional por ahora)
if __name__ == '__main__':
    app.run(debug=True)