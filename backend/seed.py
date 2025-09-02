# Este script es nuestra "migración inicial". Prepara la base de datos.
import sys
from models import create_category

def run_seed():
    print("🌱 Empezando la siembra de datos iniciales...")

    # 1. Crear algunas categorías
    print("   -> Creando coleccion de Categorías...")
    create_category(name="Desinfectantes", description="Productos para eliminar gérmenes y bacterias.")
    create_category(name="Jabones y Detergentes", description="Productos para limpieza y lavado.")
    create_category(name="Papelería", description="Toallas de papel, papel higiénico, etc.")

    print("✅ Categorías creadas.")

    # 2. Aquí podrías agregar la creación de otros datos iniciales

    print("🎉 ¡Siembra completada!")

    sys.exit(0) 

if __name__ == '__main__':
    run_seed()