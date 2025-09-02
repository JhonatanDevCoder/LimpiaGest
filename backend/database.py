import firebase_admin
from firebase_admin import credentials, firestore

print("🔥 Inicializando conexión con Firebase...")
cred = credentials.Certificate("credentials.json") 
firebase_admin.initialize_app(cred)

db = firestore.client()
print("✅ Conexión con Firebase establecida.")