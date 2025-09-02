import sys
from database import db 

def seed_categories():
    print("   -> Verificando y sembrando Categorías...")
    
    # Lista de categorías que queremos que existan
    default_categories = [
        {'name': "Desinfectantes", 'description': "Productos para eliminar gérmenes y bacterias."},
        {'name': "Jabones y Detergentes", 'description': "Productos para limpieza y lavado."},
        {'name': "Papelería", 'description': "Toallas de papel, papel higiénico, etc."}
    ]
    
    for category_data in default_categories:
        # Por cada categoría, primero buscamos si ya existe una con ese nombre
        category_name = category_data['name']
        query = db.collection('categories').where('name', '==', category_name).limit(1).get()
        
        # Si la consulta (query) devuelve una lista vacía, significa que no existe
        if not query:
            print(f"      📦 Creando categoría: {category_name}")
            db.collection('categories').add(category_data)
        else:
            print(f"      👍 La categoría '{category_name}' ya existe. Saltando.")

def run_seed():
    print("🌱 Empezando la siembra de datos iniciales...")
    seed_categories()
    print("🎉 ¡Siembra completada!")
    sys.exit(0) 

if __name__ == '__main__':
    run_seed()