import sys
from database import db
from datetime import datetime, timedelta

# --- ========================================================== ---
# ---           FUNCIÓN DE AYUDA GENÉRICA (HELPER)             ---
# --- ========================================================== ---

def seed_collection(collection_name, default_items, unique_key):
    """
    Función genérica para sembrar una colección.
    Verifica si un documento con una clave única ya existe antes de crearlo.
    Devuelve los IDs de los documentos creados o encontrados.
    """
    print(f"  -> Verificando y sembrando '{collection_name}'...")
    created_ids = {}
    for item_data in default_items:
        unique_value = item_data[unique_key]
        query = db.collection(collection_name).where(unique_key, '==', unique_value).limit(1).get()
        
        if not query:
            print(f"     📦 Creando: {unique_value}")
            _, doc_ref = db.collection(collection_name).add(item_data)
            created_ids[unique_value] = doc_ref.id
        else:
            print(f"     👍 '{unique_value}' ya existe. Obteniendo ID.")
            created_ids[unique_value] = query[0].id
            
    return created_ids

# --- ========================================================== ---
# ---           EJECUCIÓN PRINCIPAL DE SIEMBRA                 ---
# --- ========================================================== ---

def run_seed():
    print("🌱 Empezando la siembra de datos iniciales para LimpiaGest...")
    
    # --- NIVEL 1: COLECCIONES SIN DEPENDENCIAS ---
    
    category_ids = seed_collection('Categories', [
        {'name': "Desinfectantes", 'description': "Productos para eliminar gérmenes y bacterias."},
        {'name': "Jabones y Detergentes", 'description': "Productos para limpieza y lavado."},
        {'name': "Papelería", 'description': "Toallas de papel, papel higiénico, etc."},
        {'name': "Herramientas y Utensilios", 'description': "Traperos, escobas, baldes, guantes, etc."},
        {'name': "Ambientadores", 'description': "Productos para aromatizar espacios."}
    ], 'name')

    role_ids = seed_collection('Roles', [
        {'name': "Administrador", 'description': "Acceso total al sistema."},
        {'name': "Jefe de Almacén", 'description': "Gestiona inventario y operarios."},
        {'name': "Operario", 'description': "Realiza movimientos de inventario."},
        {'name': "Gerente General", 'description': "Acceso a reportes y vistas generales."},
        {'name': "Auditor", 'description': "Acceso de solo lectura para auditorías."}
    ], 'name')

    permission_ids = seed_collection('Permissions', [
        {'name': "manage_users", 'description': "Puede crear, editar y eliminar usuarios."},
        {'name': "manage_inventory", 'description': "Puede registrar entradas, salidas y ajustes."},
        {'name': "view_reports", 'description': "Puede ver los reportes de inventario."},
        {'name': "manage_suppliers", 'description': "Puede gestionar proveedores."},
        {'name': "approve_disposals", 'description': "Puede aprobar la baja de productos vencidos."}
    ], 'name')
    
    state_ids = seed_collection('States', [
        {'name': "Cundinamarca"}, {'name': "Antioquia"}, {'name': "Valle del Cauca"}, {'name': "Atlántico"}, {'name': "Santander"}
    ], 'name')
    
    handler_ids = seed_collection('EnvironmentalHandlers', [
        {'name': "EcoRecicla SAS", 'certification_code': "CERT-ECO-123", 'contact_person': "Sofia Vergara", 'phone_number': "3001112233"},
        {'name': "Gestión Ambiental S.A.", 'certification_code': "CERT-GA-456", 'contact_person': "Carlos Nieto", 'phone_number': "3014445566"},
        {'name': "BioResiduos Colombia", 'certification_code': "CERT-BIO-789", 'contact_person': "Laura Paez", 'phone_number': "3027778899"},
        {'name': "Soluciones Verdes Ltda.", 'certification_code': "CERT-SV-101", 'contact_person': "Andres Mora", 'phone_number': "3101234567"},
        {'name': "Planeta Limpio Co.", 'certification_code': "CERT-PL-202", 'contact_person': "Maria Rojas", 'phone_number': "3209876543"}
    ], 'name')

    supplier_ids = seed_collection('Suppliers', [
        {'company_name': "Químicos Industriales G&L", 'tax_id': "900.123.456-7", 'company_address': "Zona Industrial Montevideo"},
        {'company_name': "DistriLimpieza Colombia", 'tax_id': "800.789.123-4", 'company_address': "Parque Industrial Celta"},
        {'company_name': "Insumos y Químicos de la Sabana", 'tax_id': "901.234.567-8", 'company_address': "Km 2 Vía Siberia"},
        {'company_name': "Aseo Total S.A.S", 'tax_id': "801.987.654-3", 'company_address': "Calle 80 # 78 - 15"},
        {'company_name': "Proveedor Institucional Ltda.", 'tax_id': "902.345.678-9", 'company_address': "Zona Franca, Fontibón"}
    ], 'company_name')
    
    movement_type_ids = seed_collection('MovementTypes', [
        {'name': "Ingreso", 'description': "Entrada de mercancía por compra a proveedor."},
        {'name': "Salida", 'description': "Salida de mercancía para uso interno o venta."},
        {'name': "Ajuste", 'description': "Ajuste de inventario por conteo físico."},
        {'name': "Baja por Vencimiento", 'description': "Producto dado de baja por fecha de caducidad."},
        {'name': "Baja por Daño", 'description': "Producto dado de baja por estar dañado."}
    ], 'name')

    # --- NIVEL 2: COLECCIONES CON DEPENDENCIAS DE NIVEL 1 ---
    
    city_ids = seed_collection('Cities', [
        {'name': "Bogotá", 'state_id': state_ids.get("Cundinamarca")},
        {'name': "Medellín", 'state_id': state_ids.get("Antioquia")},
        {'name': "Cali", 'state_id': state_ids.get("Valle del Cauca")},
        {'name': "Barranquilla", 'state_id': state_ids.get("Atlántico")},
        {'name': "Bucaramanga", 'state_id': state_ids.get("Santander")}
    ], 'name')

    product_ids = seed_collection('Products', [
        {"sku": "DES-ALC-001", "name": "Alcohol Antiséptico 70% Litro", "stock_min": 20, "stock_max": 100, "category_id": category_ids.get("Desinfectantes"), "created_at": datetime.now()},
        {"sku": "JAB-MUL-005", "name": "Jabón Multiusos 5L", "stock_min": 10, "stock_max": 40, "category_id": category_ids.get("Jabones y Detergentes"), "created_at": datetime.now()},
        {"sku": "PAP-TOA-250", "name": "Toalla de Papel Industrial x 250m", "stock_min": 50, "stock_max": 200, "category_id": category_ids.get("Papelería"), "created_at": datetime.now()},
        {"sku": "HER-TRA-002", "name": "Trapero de Microfibra Industrial", "stock_min": 30, "stock_max": 100, "category_id": category_ids.get("Herramientas y Utensilios"), "created_at": datetime.now()},
        {"sku": "AMB-LAV-500", "name": "Ambientador Lavanda Aerosol 500ml", "stock_min": 25, "stock_max": 80, "category_id": category_ids.get("Ambientadores"), "created_at": datetime.now()}
    ], 'sku')

    # --- NIVEL 3: COLECCIONES CON DEPENDENCIAS ---

    person_ids = seed_collection('Persons', [
        {"firstname": "Jhonatan", "lastname": "Developer", "address": "Calle Falsa 123", "phone": "3109876543", "city_id": city_ids.get("Bogotá")},
        {"firstname": "Catalina", "lastname": "Manager", "address": "Av Siempre Viva 742", "phone": "3201112233", "city_id": city_ids.get("Medellín")},
        {"firstname": "Carlos", "lastname": "Ruiz", "address": "Carrera 10 # 20-30", "phone": "3112223344", "city_id": city_ids.get("Cali")},
        {"firstname": "Ana", "lastname": "Gómez", "address": "Calle 45 # 15-10", "phone": "3125556677", "city_id": city_ids.get("Barranquilla")},
        {"firstname": "Luis", "lastname": "Fernández", "address": "Transversal 5 # 50-05", "phone": "3138889900", "city_id": city_ids.get("Bucaramanga")}
    ], 'phone')

    # --- NIVEL 4: COLECCIONES CON DEPENDENCIAS ---

    user_ids = seed_collection('Users', [
        {"person_id": person_ids.get("3109876543"), "email": "admin@limpiagest.com", "password_hash": "hash-seguro-admin", "is_active": True, "created_at": datetime.now()},
        {"person_id": person_ids.get("3201112233"), "email": "manager@limpiagest.com", "password_hash": "hash-seguro-manager", "is_active": True, "created_at": datetime.now()},
        {"person_id": person_ids.get("3112223344"), "email": "operario1@limpiagest.com", "password_hash": "hash-seguro-op1", "is_active": True, "created_at": datetime.now()},
        {"person_id": person_ids.get("3125556677"), "email": "gerente@limpiagest.com", "password_hash": "hash-seguro-gerente", "is_active": True, "created_at": datetime.now()},
        {"person_id": person_ids.get("3138889900"), "email": "auditor@limpiagest.com", "password_hash": "hash-seguro-auditor", "is_active": False, "created_at": datetime.now()}
    ], 'email')
    
    batch_ids = seed_collection('InventoryBatches', [
        {"product_id": product_ids.get("DES-ALC-001"), "supplier_id": supplier_ids.get("Químicos Industriales G&L"), "lot_number": "LOTE-2025-A01", "initial_quantity": 100, "quantity_on_hand": 80, "expiration_date": datetime(2026, 9, 10), "received_at": datetime.now() - timedelta(days=30)},
        {"product_id": product_ids.get("JAB-MUL-005"), "supplier_id": supplier_ids.get("DistriLimpieza Colombia"), "lot_number": "LOTE-2025-B02", "initial_quantity": 40, "quantity_on_hand": 40, "expiration_date": datetime(2027, 1, 15), "received_at": datetime.now() - timedelta(days=20)},
        {"product_id": product_ids.get("PAP-TOA-250"), "supplier_id": supplier_ids.get("Proveedor Institucional Ltda."), "lot_number": "LOTE-2025-C03", "initial_quantity": 200, "quantity_on_hand": 150, "expiration_date": None, "received_at": datetime.now() - timedelta(days=10)},
        {"product_id": product_ids.get("HER-TRA-002"), "supplier_id": supplier_ids.get("Aseo Total S.A.S"), "lot_number": "LOTE-2025-D04", "initial_quantity": 50, "quantity_on_hand": 50, "expiration_date": None, "received_at": datetime.now() - timedelta(days=5)},
        {"product_id": product_ids.get("AMB-LAV-500"), "supplier_id": supplier_ids.get("Insumos y Químicos de la Sabana"), "lot_number": "LOTE-2025-E05", "initial_quantity": 80, "quantity_on_hand": 70, "expiration_date": datetime(2026, 12, 1), "received_at": datetime.now() - timedelta(days=2)}
    ], 'lot_number')

    # --- NIVEL 5: DATOS FINALES ---
    
    seed_collection('InventoryMovements', [
        {"batch_id": batch_ids.get("LOTE-2025-A01"), "user_id": user_ids.get("operario1@limpiagest.com"), "movement_type_id": movement_type_ids.get("Salida"), "quantity_changed": -20, "movement_date": datetime.now() - timedelta(days=15)},
        {"batch_id": batch_ids.get("LOTE-2025-B02"), "user_id": user_ids.get("manager@limpiagest.com"), "movement_type_id": movement_type_ids.get("Ingreso"), "quantity_changed": 40, "movement_date": datetime.now() - timedelta(days=20)},
        {"batch_id": batch_ids.get("LOTE-2025-C03"), "user_id": user_ids.get("operario1@limpiagest.com"), "movement_type_id": movement_type_ids.get("Salida"), "quantity_changed": -50, "movement_date": datetime.now() - timedelta(days=5)},
        {"batch_id": batch_ids.get("LOTE-2025-D04"), "user_id": user_ids.get("manager@limpiagest.com"), "movement_type_id": movement_type_ids.get("Ingreso"), "quantity_changed": 50, "movement_date": datetime.now() - timedelta(days=5)},
        {"batch_id": batch_ids.get("LOTE-2025-E05"), "user_id": user_ids.get("operario1@limpiagest.com"), "movement_type_id": movement_type_ids.get("Salida"), "quantity_changed": -10, "movement_date": datetime.now() - timedelta(days=1)}
    ], 'movement_date')

    seed_collection('Stock', [
        {"product_id": product_ids.get("DES-ALC-001"), "total_quantity_on_hand": 80},
        {"product_id": product_ids.get("JAB-MUL-005"), "total_quantity_on_hand": 40},
        {"product_id": product_ids.get("PAP-TOA-250"), "total_quantity_on_hand": 150},
        {"product_id": product_ids.get("HER-TRA-002"), "total_quantity_on_hand": 50},
        {"product_id": product_ids.get("AMB-LAV-500"), "total_quantity_on_hand": 70}
    ], 'product_id')

    # Colecciones que se llenarán con el uso de la app
    print("  -> Las colecciones 'Alerts' y 'DisposalLog' se crearán vacías y se llenarán con el uso de la aplicación.")
    
    print("\n🎉 ¡Siembra de datos completada!")
    print("✅ Tu base de datos ahora tiene al menos 5 registros en 10 colecciones diferentes.")

if __name__ == '__main__':
    run_seed()
