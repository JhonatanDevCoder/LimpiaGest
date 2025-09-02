from app import db # Importamos la conexión a la DB desde nuestra app

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