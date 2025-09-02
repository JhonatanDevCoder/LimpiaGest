from database import db

def create_category(name, description):

    print(f"📦 Creando categoría: {name}")
    category_data = {
        'name': name,
        'description': description
    }
    # Crea un nuevo documento en la colección "categories"
    db.collection('categories').add(category_data)
    return category_data

def create_product(sku, name, description, stock_min, stock_max, category_id):

    print(f"🧼 Creando producto: {name}")
    product_data = {
        'sku': sku,
        'name': name,
        'description': description,
        'stock_min': stock_min,
        'stock_max': stock_max,
        'category_id': category_id # Guardamos la referencia a su categoría
    }
    db.collection('products').add(product_data)
    return product_data

def get_all_categories():
    
    print("🔍 Buscando todas las categorías en Firebase...")

    # 1. Apunta a la colección 'categories' y trae todos los documentos
    categories_ref = db.collection('categories').stream()

    # 2. Prepara una lista vacía para guardar los resultados
    categories = []

    # 3. Recorre cada documento que encontró en la base de datos
    for category in categories_ref:
        category_data = category.to_dict()
        category_data['id'] = category.id
        categories.append(category_data)

    print(f"   -> Se encontraron {len(categories)} categorías.")
    return categories