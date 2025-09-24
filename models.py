from database import db

def _get_all(collection_name):
    try:
        collection_ref = db.collection(collection_name)
        docs = collection_ref.stream()
        items = []
        for doc in docs:
            item_data = doc.to_dict()
            item_data['id'] = doc.id
            items.append(item_data)
        return items
    except Exception as e:
        print(f"Error al obtener todos los documentos de {collection_name}: {e}")
        return []

def _get_by_id(collection_name, doc_id):
    try:
        doc_ref = db.collection(collection_name).document(doc_id)
        doc = doc_ref.get()
        if doc.exists:
            item_data = doc.to_dict()
            item_data['id'] = doc.id
            return item_data
        return None
    except Exception as e:
        print(f"Error al obtener el documento {doc_id} de {collection_name}: {e}")
        return None

def _create(collection_name, data):
    try:
        db.collection(collection_name).add(data)
        return True
    except Exception as e:
        print(f"Error al crear un documento en {collection_name}: {e}")
        return False

def _update(collection_name, doc_id, data):
    try:
        db.collection(collection_name).document(doc_id).update(data)
        return True
    except Exception as e:
        print(f"Error al actualizar el documento {doc_id} en {collection_name}: {e}")
        return False

def _delete(collection_name, doc_id):
    try:
        db.collection(collection_name).document(doc_id).delete()
        return True
    except Exception as e:
        print(f"Error al eliminar el documento {doc_id} en {collection_name}: {e}")
        return False

# --- Categories ---
def get_all_categories(): return _get_all('Categories')
def get_category_by_id(id): return _get_by_id('Categories', id)
def create_category(data): return _create('Categories', data)
def update_category(id, data): return _update('Categories', id, data)
def delete_category(id): return _delete('Categories', id)

# --- Products ---
def get_all_products(): return _get_all('Products')
def get_product_by_id(id): return _get_by_id('Products', id)
def create_product(data): return _create('Products', data)
def update_product(id, data): return _update('Products', id, data)
def delete_product(id): return _delete('Products', id)

# --- Suppliers ---
def get_all_suppliers(): return _get_all('Suppliers')
def get_supplier_by_id(id): return _get_by_id('Suppliers', id)
def create_supplier(data): return _create('Suppliers', data)
def update_supplier(id, data): return _update('Suppliers', id, data)
def delete_supplier(id): return _delete('Suppliers', id)

# --- Persons ---
def get_all_persons(): return _get_all('Persons')
def get_person_by_id(id): return _get_by_id('Persons', id)
def create_person(data): return _create('Persons', data)
def update_person(id, data): return _update('Persons', id, data)
def delete_person(id): return _delete('Persons', id)

# --- Users ---
def get_all_users(): return _get_all('Users')
def get_user_by_id(id): return _get_by_id('Users', id)
def create_user(data): return _create('Users', data)
def update_user(id, data): return _update('Users', id, data)
def delete_user(id): return _delete('Users', id)

# --- InventoryBatches ---
def get_all_inventory_batches(): return _get_all('InventoryBatches')
def get_inventory_batch_by_id(id): return _get_by_id('InventoryBatches', id)
def create_inventory_batch(data): return _create('InventoryBatches', data)
def update_inventory_batch(id, data): return _update('InventoryBatches', id, data)
def delete_inventory_batch(id): return _delete('InventoryBatches', id)

# --- Inventory Movements ---
def get_all_inventory_movements(): return _get_all('Inventory Movements')
def get_inventory_movement_by_id(id): return _get_by_id('Inventory Movements', id)
def create_inventory_movement(data): return _create('Inventory Movements', data)
def update_inventory_movement(id, data): return _update('Inventory Movements', id, data)
def delete_inventory_movement(id): return _delete('Inventory Movements', id)

# --- Stock ---
def get_all_stock(): return _get_all('Stock')
def get_stock_by_id(id): return _get_by_id('Stock', id)
def create_stock(data): return _create('Stock', data)
def update_stock(id, data): return _update('Stock', id, data)
def delete_stock(id): return _delete('Stock', id)

# --- Alerts ---
def get_all_alerts(): return _get_all('Alerts')
def get_alert_by_id(id): return _get_by_id('Alerts', id)
def create_alert(data): return _create('Alerts', data)
def update_alert(id, data): return _update('Alerts', id, data)
def delete_alert(id): return _delete('Alerts', id)

# --- DisposalLog ---
def get_all_disposal_logs(): return _get_all('DisposalLog')
def get_disposal_log_by_id(id): return _get_by_id('DisposalLog', id)
def create_disposal_log(data): return _create('DisposalLog', data)
def update_disposal_log(id, data): return _update('DisposalLog', id, data)
def delete_disposal_log(id): return _delete('DisposalLog', id)

# --- EnvironmentalHandlers ---
def get_all_environmental_handlers(): return _get_all('EnvironmentalHandlers')
def get_environmental_handler_by_id(id): return _get_by_id('EnvironmentalHandlers', id)
def create_environmental_handler(data): return _create('EnvironmentalHandlers', data)
def update_environmental_handler(id, data): return _update('EnvironmentalHandlers', id, data)
def delete_environmental_handler(id): return _delete('EnvironmentalHandlers', id)

# --- Roles ---
def get_all_roles(): return _get_all('Roles')
def get_role_by_id(id): return _get_by_id('Roles', id)
def create_role(data): return _create('Roles', data)
def update_role(id, data): return _update('Roles', id, data)
def delete_role(id): return _delete('Roles', id)

# --- Permissions ---
def get_all_permissions(): return _get_all('Permissions')
def get_permission_by_id(id): return _get_by_id('Permissions', id)
def create_permission(data): return _create('Permissions', data)
def update_permission(id, data): return _update('Permissions', id, data)
def delete_permission(id): return _delete('Permissions', id)

# --- States ---
def get_all_states(): return _get_all('States')
def get_state_by_id(id): return _get_by_id('States', id)
def create_state(data): return _create('States', data)
def update_state(id, data): return _update('States', id, data)
def delete_state(id): return _delete('States', id)

# --- Cities ---
def get_all_cities(): return _get_all('Cities')
def get_city_by_id(id): return _get_by_id('Cities', id)
def create_city(data): return _create('Cities', data)
def update_city(id, data): return _update('Cities', id, data)
def delete_city(id): return _delete('Cities', id)

# --- UserRoles ---
def get_all_user_roles(): return _get_all('UserRoles')
def create_user_role(data): return _create('UserRoles', data)
def delete_user_role(id): return _delete('UserRoles', id)

# --- RolePermissions ---
def get_all_role_permissions(): return _get_all('RolePermissions')
def create_role_permission(data): return _create('RolePermissions', data)
def delete_role_permission(id): return _delete('RolePermissions', id)