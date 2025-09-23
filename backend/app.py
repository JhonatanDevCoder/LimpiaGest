from flask import Flask, jsonify, request
import json
from flasgger import Swagger
from models import *

app = Flask(__name__)
swagger = Swagger(app)

def _get_request_data():
    """Obtiene y decodifica los datos del cuerpo de la petición."""
    raw_data = request.data
    decoded_data = raw_data.decode('latin-1')
    return json.loads(decoded_data)

# --- RUTA PRINCIPAL ---
@app.route('/', methods=['GET'])
def index():
    """
    Endpoint de bienvenida de la API.
    ---
    tags: [General]
    """
    return jsonify({
        "mensaje": "¡Bienvenido a la API de LimpiaGest!",
        "documentacion_api": "/apidocs/"
    })

# --- ================================================== ---
# ---                   CATEGORIES                       ---
# --- ================================================== ---

@app.route('/api/categories', methods=['GET'])
def get_all_categories_route():
    """
    Obtiene todas las categorías.
    ---
    tags: [Categories]
    """
    items = get_all_categories()
    return jsonify(items), 200

@app.route('/api/categories', methods=['POST'])
def create_category_route():
    """
    Crea una nueva categoría.
    ---
    tags: [Categories]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_category(data)
    return jsonify({"success": "Categoría creada"}), 201

@app.route('/api/categories/<string:item_id>', methods=['GET'])
def get_category_by_id_route(item_id):
    """
    Obtiene una categoría por su ID.
    ---
    tags: [Categories]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    item = get_category_by_id(item_id)
    return jsonify(item) if item else (jsonify({"error": "No encontrado"}), 404)

@app.route('/api/categories/<string:item_id>', methods=['PUT'])
def update_category_route(item_id):
    """
    Actualiza una categoría.
    ---
    tags: [Categories]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    update_category(item_id, data)
    return jsonify({"success": "Categoría actualizada"}), 200

@app.route('/api/categories/<string:item_id>', methods=['DELETE'])
def delete_category_route(item_id):
    """
    Elimina una categoría.
    ---
    tags: [Categories]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_category(item_id)
    return jsonify({"success": "Categoría eliminada"}), 200

# --- ================================================== ---
# ---                     PRODUCTS                       ---
# --- ================================================== ---

@app.route('/api/products', methods=['GET'])
def get_all_products_route():
    """
    Obtiene todos los productos.
    ---
    tags: [Products]
    """
    items = get_all_products()
    return jsonify(items), 200

@app.route('/api/products', methods=['POST'])
def create_product_route():
    """
    Crea un nuevo producto.
    ---
    tags: [Products]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_product(data)
    return jsonify({"success": "Producto creado"}), 201

@app.route('/api/products/<string:item_id>', methods=['GET'])
def get_product_by_id_route(item_id):
    """
    Obtiene un producto por su ID.
    ---
    tags: [Products]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    item = get_product_by_id(item_id)
    return jsonify(item) if item else (jsonify({"error": "No encontrado"}), 404)

@app.route('/api/products/<string:item_id>', methods=['PUT'])
def update_product_route(item_id):
    """
    Actualiza un producto.
    ---
    tags: [Products]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    update_product(item_id, data)
    return jsonify({"success": "Producto actualizado"}), 200

@app.route('/api/products/<string:item_id>', methods=['DELETE'])
def delete_product_route(item_id):
    """
    Elimina un producto.
    ---
    tags: [Products]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_product(item_id)
    return jsonify({"success": "Producto eliminado"}), 200
    
# --- ================================================== ---
# ---                    SUPPLIERS                       ---
# --- ================================================== ---

@app.route('/api/suppliers', methods=['GET'])
def get_all_suppliers_route():
    """
    Obtiene todos los proveedores.
    ---
    tags: [Suppliers]
    """
    items = get_all_suppliers()
    return jsonify(items), 200

@app.route('/api/suppliers', methods=['POST'])
def create_supplier_route():
    """
    Crea un nuevo proveedor.
    ---
    tags: [Suppliers]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_supplier(data)
    return jsonify({"success": "Proveedor creado"}), 201

@app.route('/api/suppliers/<string:item_id>', methods=['GET'])
def get_supplier_by_id_route(item_id):
    """
    Obtiene un proveedor por su ID.
    ---
    tags: [Suppliers]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    item = get_supplier_by_id(item_id)
    return jsonify(item) if item else (jsonify({"error": "No encontrado"}), 404)

@app.route('/api/suppliers/<string:item_id>', methods=['PUT'])
def update_supplier_route(item_id):
    """
    Actualiza un proveedor.
    ---
    tags: [Suppliers]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    update_supplier(item_id, data)
    return jsonify({"success": "Proveedor actualizado"}), 200

@app.route('/api/suppliers/<string:item_id>', methods=['DELETE'])
def delete_supplier_route(item_id):
    """
    Elimina un proveedor.
    ---
    tags: [Suppliers]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_supplier(item_id)
    return jsonify({"success": "Proveedor eliminado"}), 200

# --- ================================================== ---
# ---                      PERSONS                       ---
# --- ================================================== ---

@app.route('/api/persons', methods=['GET'])
def get_all_persons_route():
    """
    Obtiene todas las personas.
    ---
    tags: [Persons]
    """
    items = get_all_persons()
    return jsonify(items), 200

@app.route('/api/persons', methods=['POST'])
def create_person_route():
    """
    Crea una nueva persona.
    ---
    tags: [Persons]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_person(data)
    return jsonify({"success": "Persona creada"}), 201

@app.route('/api/persons/<string:item_id>', methods=['GET'])
def get_person_by_id_route(item_id):
    """
    Obtiene una persona por su ID.
    ---
    tags: [Persons]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    item = get_person_by_id(item_id)
    return jsonify(item) if item else (jsonify({"error": "No encontrado"}), 404)

@app.route('/api/persons/<string:item_id>', methods=['PUT'])
def update_person_route(item_id):
    """
    Actualiza una persona.
    ---
    tags: [Persons]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    update_person(item_id, data)
    return jsonify({"success": "Persona actualizada"}), 200

@app.route('/api/persons/<string:item_id>', methods=['DELETE'])
def delete_person_route(item_id):
    """
    Elimina una persona.
    ---
    tags: [Persons]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_person(item_id)
    return jsonify({"success": "Persona eliminada"}), 200

# --- ================================================== ---
# ---                       USERS                        ---
# --- ================================================== ---

@app.route('/api/users', methods=['GET'])
def get_all_users_route():
    """
    Obtiene todos los usuarios.
    ---
    tags: [Users]
    """
    items = get_all_users()
    return jsonify(items), 200

@app.route('/api/users', methods=['POST'])
def create_user_route():
    """
    Crea un nuevo usuario.
    ---
    tags: [Users]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_user(data)
    return jsonify({"success": "Usuario creado"}), 201

@app.route('/api/users/<string:item_id>', methods=['GET'])
def get_user_by_id_route(item_id):
    """
    Obtiene un usuario por su ID.
    ---
    tags: [Users]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    item = get_user_by_id(item_id)
    return jsonify(item) if item else (jsonify({"error": "No encontrado"}), 404)

@app.route('/api/users/<string:item_id>', methods=['PUT'])
def update_user_route(item_id):
    """
    Actualiza un usuario.
    ---
    tags: [Users]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    update_user(item_id, data)
    return jsonify({"success": "Usuario actualizado"}), 200

@app.route('/api/users/<string:item_id>', methods=['DELETE'])
def delete_user_route(item_id):
    """
    Elimina un usuario.
    ---
    tags: [Users]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_user(item_id)
    return jsonify({"success": "Usuario eliminado"}), 200

# --- ================================================== ---
# ---                 INVENTORY BATCHES                  ---
# --- ================================================== ---

@app.route('/api/inventory-batches', methods=['GET'])
def get_all_inventory_batches_route():
    """
    Obtiene todos los lotes de inventario.
    ---
    tags: [InventoryBatches]
    """
    items = get_all_inventory_batches()
    return jsonify(items), 200

@app.route('/api/inventory-batches', methods=['POST'])
def create_inventory_batch_route():
    """
    Crea un nuevo lote de inventario.
    ---
    tags: [InventoryBatches]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_inventory_batch(data)
    return jsonify({"success": "Lote de inventario creado"}), 201

@app.route('/api/inventory-batches/<string:item_id>', methods=['GET'])
def get_inventory_batch_by_id_route(item_id):
    """
    Obtiene un lote de inventario por su ID.
    ---
    tags: [InventoryBatches]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    item = get_inventory_batch_by_id(item_id)
    return jsonify(item) if item else (jsonify({"error": "No encontrado"}), 404)

@app.route('/api/inventory-batches/<string:item_id>', methods=['PUT'])
def update_inventory_batch_route(item_id):
    """
    Actualiza un lote de inventario.
    ---
    tags: [InventoryBatches]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    update_inventory_batch(item_id, data)
    return jsonify({"success": "Lote de inventario actualizado"}), 200

@app.route('/api/inventory-batches/<string:item_id>', methods=['DELETE'])
def delete_inventory_batch_route(item_id):
    """
    Elimina un lote de inventario.
    ---
    tags: [InventoryBatches]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_inventory_batch(item_id)
    return jsonify({"success": "Lote de inventario eliminado"}), 200

# --- ================================================== ---
# ---               INVENTORY MOVEMENTS                  ---
# --- ================================================== ---

@app.route('/api/inventory-movements', methods=['GET'])
def get_all_inventory_movements_route():
    """
    Obtiene todos los movimientos de inventario.
    ---
    tags: [InventoryMovements]
    """
    items = get_all_inventory_movements()
    return jsonify(items), 200

@app.route('/api/inventory-movements', methods=['POST'])
def create_inventory_movement_route():
    """
    Crea un nuevo movimiento de inventario.
    ---
    tags: [InventoryMovements]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_inventory_movement(data)
    return jsonify({"success": "Movimiento de inventario creado"}), 201

@app.route('/api/inventory-movements/<string:item_id>', methods=['GET'])
def get_inventory_movement_by_id_route(item_id):
    """
    Obtiene un movimiento de inventario por su ID.
    ---
    tags: [InventoryMovements]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    item = get_inventory_movement_by_id(item_id)
    return jsonify(item) if item else (jsonify({"error": "No encontrado"}), 404)

@app.route('/api/inventory-movements/<string:item_id>', methods=['PUT'])
def update_inventory_movement_route(item_id):
    """
    Actualiza un movimiento de inventario.
    ---
    tags: [InventoryMovements]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    update_inventory_movement(item_id, data)
    return jsonify({"success": "Movimiento de inventario actualizado"}), 200

@app.route('/api/inventory-movements/<string:item_id>', methods=['DELETE'])
def delete_inventory_movement_route(item_id):
    """
    Elimina un movimiento de inventario.
    ---
    tags: [InventoryMovements]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_inventory_movement(item_id)
    return jsonify({"success": "Movimiento de inventario eliminado"}), 200

# --- ================================================== ---
# ---                        STOCK                       ---
# --- ================================================== ---

@app.route('/api/stock', methods=['GET'])
def get_all_stock_route():
    """
    Obtiene todo el stock.
    ---
    tags: [Stock]
    """
    items = get_all_stock()
    return jsonify(items), 200

@app.route('/api/stock', methods=['POST'])
def create_stock_route():
    """
    Crea un nuevo registro de stock.
    ---
    tags: [Stock]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_stock(data)
    return jsonify({"success": "Registro de stock creado"}), 201

@app.route('/api/stock/<string:item_id>', methods=['GET'])
def get_stock_by_id_route(item_id):
    """
    Obtiene un registro de stock por su ID.
    ---
    tags: [Stock]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    item = get_stock_by_id(item_id)
    return jsonify(item) if item else (jsonify({"error": "No encontrado"}), 404)

@app.route('/api/stock/<string:item_id>', methods=['PUT'])
def update_stock_route(item_id):
    """
    Actualiza un registro de stock.
    ---
    tags: [Stock]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    update_stock(item_id, data)
    return jsonify({"success": "Registro de stock actualizado"}), 200

@app.route('/api/stock/<string:item_id>', methods=['DELETE'])
def delete_stock_route(item_id):
    """
    Elimina un registro de stock.
    ---
    tags: [Stock]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_stock(item_id)
    return jsonify({"success": "Registro de stock eliminado"}), 200

# --- ================================================== ---
# ---                       ALERTS                       ---
# --- ================================================== ---

@app.route('/api/alerts', methods=['GET'])
def get_all_alerts_route():
    """
    Obtiene todas las alertas.
    ---
    tags: [Alerts]
    """
    items = get_all_alerts()
    return jsonify(items), 200

@app.route('/api/alerts', methods=['POST'])
def create_alert_route():
    """
    Crea una nueva alerta.
    ---
    tags: [Alerts]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_alert(data)
    return jsonify({"success": "Alerta creada"}), 201

@app.route('/api/alerts/<string:item_id>', methods=['GET'])
def get_alert_by_id_route(item_id):
    """
    Obtiene una alerta por su ID.
    ---
    tags: [Alerts]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    item = get_alert_by_id(item_id)
    return jsonify(item) if item else (jsonify({"error": "No encontrado"}), 404)

@app.route('/api/alerts/<string:item_id>', methods=['PUT'])
def update_alert_route(item_id):
    """
    Actualiza una alerta.
    ---
    tags: [Alerts]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    update_alert(item_id, data)
    return jsonify({"success": "Alerta actualizada"}), 200

@app.route('/api/alerts/<string:item_id>', methods=['DELETE'])
def delete_alert_route(item_id):
    """
    Elimina una alerta.
    ---
    tags: [Alerts]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_alert(item_id)
    return jsonify({"success": "Alerta eliminada"}), 200

# --- ================================================== ---
# ---                    DISPOSAL LOG                    ---
# --- ================================================== ---

@app.route('/api/disposal-logs', methods=['GET'])
def get_all_disposal_logs_route():
    """
    Obtiene todos los registros de desecho.
    ---
    tags: [DisposalLog]
    """
    items = get_all_disposal_logs()
    return jsonify(items), 200

@app.route('/api/disposal-logs', methods=['POST'])
def create_disposal_log_route():
    """
    Crea un nuevo registro de desecho.
    ---
    tags: [DisposalLog]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_disposal_log(data)
    return jsonify({"success": "Registro de desecho creado"}), 201

@app.route('/api/disposal-logs/<string:item_id>', methods=['GET'])
def get_disposal_log_by_id_route(item_id):
    """
    Obtiene un registro de desecho por su ID.
    ---
    tags: [DisposalLog]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    item = get_disposal_log_by_id(item_id)
    return jsonify(item) if item else (jsonify({"error": "No encontrado"}), 404)

@app.route('/api/disposal-logs/<string:item_id>', methods=['PUT'])
def update_disposal_log_route(item_id):
    """
    Actualiza un registro de desecho.
    ---
    tags: [DisposalLog]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    update_disposal_log(item_id, data)
    return jsonify({"success": "Registro de desecho actualizado"}), 200

@app.route('/api/disposal-logs/<string:item_id>', methods=['DELETE'])
def delete_disposal_log_route(item_id):
    """
    Elimina un registro de desecho.
    ---
    tags: [DisposalLog]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_disposal_log(item_id)
    return jsonify({"success": "Registro de desecho eliminado"}), 200

# --- ================================================== ---
# ---              ENVIRONMENTAL HANDLERS                ---
# --- ================================================== ---

@app.route('/api/environmental-handlers', methods=['GET'])
def get_all_environmental_handlers_route():
    """
    Obtiene todos los gestores ambientales.
    ---
    tags: [EnvironmentalHandlers]
    """
    items = get_all_environmental_handlers()
    return jsonify(items), 200

@app.route('/api/environmental-handlers', methods=['POST'])
def create_environmental_handler_route():
    """
    Crea un nuevo gestor ambiental.
    ---
    tags: [EnvironmentalHandlers]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_environmental_handler(data)
    return jsonify({"success": "Gestor ambiental creado"}), 201

@app.route('/api/environmental-handlers/<string:item_id>', methods=['GET'])
def get_environmental_handler_by_id_route(item_id):
    """
    Obtiene un gestor ambiental por su ID.
    ---
    tags: [EnvironmentalHandlers]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    item = get_environmental_handler_by_id(item_id)
    return jsonify(item) if item else (jsonify({"error": "No encontrado"}), 404)

@app.route('/api/environmental-handlers/<string:item_id>', methods=['PUT'])
def update_environmental_handler_route(item_id):
    """
    Actualiza un gestor ambiental.
    ---
    tags: [EnvironmentalHandlers]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    update_environmental_handler(item_id, data)
    return jsonify({"success": "Gestor ambiental actualizado"}), 200

@app.route('/api/environmental-handlers/<string:item_id>', methods=['DELETE'])
def delete_environmental_handler_route(item_id):
    """
    Elimina un gestor ambiental.
    ---
    tags: [EnvironmentalHandlers]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_environmental_handler(item_id)
    return jsonify({"success": "Gestor ambiental eliminado"}), 200

# --- ================================================== ---
# ---                        ROLES                       ---
# --- ================================================== ---

@app.route('/api/roles', methods=['GET'])
def get_all_roles_route():
    """
    Obtiene todos los roles.
    ---
    tags: [Roles]
    """
    items = get_all_roles()
    return jsonify(items), 200

@app.route('/api/roles', methods=['POST'])
def create_role_route():
    """
    Crea un nuevo rol.
    ---
    tags: [Roles]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_role(data)
    return jsonify({"success": "Rol creado"}), 201

@app.route('/api/roles/<string:item_id>', methods=['GET'])
def get_role_by_id_route(item_id):
    """
    Obtiene un rol por su ID.
    ---
    tags: [Roles]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    item = get_role_by_id(item_id)
    return jsonify(item) if item else (jsonify({"error": "No encontrado"}), 404)

@app.route('/api/roles/<string:item_id>', methods=['PUT'])
def update_role_route(item_id):
    """
    Actualiza un rol.
    ---
    tags: [Roles]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    update_role(item_id, data)
    return jsonify({"success": "Rol actualizado"}), 200

@app.route('/api/roles/<string:item_id>', methods=['DELETE'])
def delete_role_route(item_id):
    """
    Elimina un rol.
    ---
    tags: [Roles]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_role(item_id)
    return jsonify({"success": "Rol eliminado"}), 200

# --- ================================================== ---
# ---                     PERMISSIONS                    ---
# --- ================================================== ---

@app.route('/api/permissions', methods=['GET'])
def get_all_permissions_route():
    """
    Obtiene todos los permisos.
    ---
    tags: [Permissions]
    """
    items = get_all_permissions()
    return jsonify(items), 200

@app.route('/api/permissions', methods=['POST'])
def create_permission_route():
    """
    Crea un nuevo permiso.
    ---
    tags: [Permissions]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_permission(data)
    return jsonify({"success": "Permiso creado"}), 201

@app.route('/api/permissions/<string:item_id>', methods=['GET'])
def get_permission_by_id_route(item_id):
    """
    Obtiene un permiso por su ID.
    ---
    tags: [Permissions]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    item = get_permission_by_id(item_id)
    return jsonify(item) if item else (jsonify({"error": "No encontrado"}), 404)

@app.route('/api/permissions/<string:item_id>', methods=['PUT'])
def update_permission_route(item_id):
    """
    Actualiza un permiso.
    ---
    tags: [Permissions]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    update_permission(item_id, data)
    return jsonify({"success": "Permiso actualizado"}), 200

@app.route('/api/permissions/<string:item_id>', methods=['DELETE'])
def delete_permission_route(item_id):
    """
    Elimina un permiso.
    ---
    tags: [Permissions]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_permission(item_id)
    return jsonify({"success": "Permiso eliminado"}), 200

# --- ================================================== ---
# ---                       STATES                       ---
# --- ================================================== ---

@app.route('/api/states', methods=['GET'])
def get_all_states_route():
    """
    Obtiene todos los estados/departamentos.
    ---
    tags: [States]
    """
    items = get_all_states()
    return jsonify(items), 200

@app.route('/api/states', methods=['POST'])
def create_state_route():
    """
    Crea un nuevo estado/departamento.
    ---
    tags: [States]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_state(data)
    return jsonify({"success": "Estado creado"}), 201

@app.route('/api/states/<string:item_id>', methods=['GET'])
def get_state_by_id_route(item_id):
    """
    Obtiene un estado/departamento por su ID.
    ---
    tags: [States]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    item = get_state_by_id(item_id)
    return jsonify(item) if item else (jsonify({"error": "No encontrado"}), 404)

@app.route('/api/states/<string:item_id>', methods=['PUT'])
def update_state_route(item_id):
    """
    Actualiza un estado/departamento.
    ---
    tags: [States]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    update_state(item_id, data)
    return jsonify({"success": "Estado actualizado"}), 200

@app.route('/api/states/<string:item_id>', methods=['DELETE'])
def delete_state_route(item_id):
    """
    Elimina un estado/departamento.
    ---
    tags: [States]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_state(item_id)
    return jsonify({"success": "Estado eliminado"}), 200

# --- ================================================== ---
# ---                       CITIES                       ---
# --- ================================================== ---

@app.route('/api/cities', methods=['GET'])
def get_all_cities_route():
    """
    Obtiene todas las ciudades.
    ---
    tags: [Cities]
    """
    items = get_all_cities()
    return jsonify(items), 200

@app.route('/api/cities', methods=['POST'])
def create_city_route():
    """
    Crea una nueva ciudad.
    ---
    tags: [Cities]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_city(data)
    return jsonify({"success": "Ciudad creada"}), 201

@app.route('/api/cities/<string:item_id>', methods=['GET'])
def get_city_by_id_route(item_id):
    """
    Obtiene una ciudad por su ID.
    ---
    tags: [Cities]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    item = get_city_by_id(item_id)
    return jsonify(item) if item else (jsonify({"error": "No encontrado"}), 404)

@app.route('/api/cities/<string:item_id>', methods=['PUT'])
def update_city_route(item_id):
    """
    Actualiza una ciudad.
    ---
    tags: [Cities]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    update_city(item_id, data)
    return jsonify({"success": "Ciudad actualizada"}), 200

@app.route('/api/cities/<string:item_id>', methods=['DELETE'])
def delete_city_route(item_id):
    """
    Elimina una ciudad.
    ---
    tags: [Cities]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_city(item_id)
    return jsonify({"success": "Ciudad eliminada"}), 200

# --- ================================================== ---
# ---                     USER ROLES                     ---
# --- ================================================== ---

@app.route('/api/user-roles', methods=['GET'])
def get_all_user_roles_route():
    """
    Obtiene todas las asignaciones de roles a usuarios.
    ---
    tags: [UserRoles]
    """
    items = get_all_user_roles()
    return jsonify(items), 200

@app.route('/api/user-roles', methods=['POST'])
def create_user_role_route():
    """
    Asigna un rol a un usuario.
    ---
    tags: [UserRoles]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_user_role(data)
    return jsonify({"success": "Rol de usuario asignado"}), 201

@app.route('/api/user-roles/<string:item_id>', methods=['DELETE'])
def delete_user_role_route(item_id):
    """
    Elimina la asignación de un rol a un usuario.
    ---
    tags: [UserRoles]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_user_role(item_id)
    return jsonify({"success": "Rol de usuario eliminado"}), 200

# --- ================================================== ---
# ---                  ROLE PERMISSIONS                  ---
# --- ================================================== ---

@app.route('/api/role-permissions', methods=['GET'])
def get_all_role_permissions_route():
    """
    Obtiene todas las asignaciones de permisos a roles.
    ---
    tags: [RolePermissions]
    """
    items = get_all_role_permissions()
    return jsonify(items), 200

@app.route('/api/role-permissions', methods=['POST'])
def create_role_permission_route():
    """
    Asigna un permiso a un rol.
    ---
    tags: [RolePermissions]
    parameters:
      - in: body
        name: body
        schema: { type: object }
    """
    data = _get_request_data()
    create_role_permission(data)
    return jsonify({"success": "Permiso de rol asignado"}), 201

@app.route('/api/role-permissions/<string:item_id>', methods=['DELETE'])
def delete_role_permission_route(item_id):
    """
    Elimina la asignación de un permiso a un rol.
    ---
    tags: [RolePermissions]
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    """
    delete_role_permission(item_id)
    return jsonify({"success": "Permiso de rol eliminado"}), 200

# --- Bloque para correr la app ---
if __name__ == '__main__':
    app.run(debug=True)

