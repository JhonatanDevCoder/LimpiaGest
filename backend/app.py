from flask import Flask, jsonify
from models import get_all_categories 

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# --- RUTAS DE LA API ---
@app.route('/')
def hello_world():
    return '¡Hola, mundo! ¡El backend de LimpiaGest está funcionando!'

@app.route('/api/categories', methods=['GET'])
def list_categories():
    all_categories = get_all_categories()
    return jsonify(all_categories), 200

@app.route('/test-db')
def test_db():
    try:
        from database import db 
        users_ref = db.collection('users').limit(1).get()
        return "✅ ¡Conexión con Firestore exitosa desde la app!"
    except Exception as e:
        return f"❌ Error conectando a Firestore: {e}"

if __name__ == '__main__':
    app.run(debug=True)