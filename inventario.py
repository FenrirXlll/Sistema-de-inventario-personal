import json
import datetime
import uuid
import funciones  # Importa el archivo funciones.py

# Nombre del archivo donde se guardan los datos del inventario
ARCHIVO_INVENTARIO = "inventario.txt"

def cargar_inventario():
    """
    Carga los datos del inventario desde el archivo JSON.
    Si el archivo no existe o está vacío, retorna una lista vacía.
    """
    try:
        with open(ARCHIVO_INVENTARIO, "r") as f:
            inventario = json.load(f)
    except FileNotFoundError:
        inventario = []
    except json.JSONDecodeError:
        inventario = []  # Archivo vacío o corrupto
    return inventario

def guardar_inventario(inventario):
    """
    Guarda los datos del inventario en el archivo JSON.
    """
    with open(ARCHIVO_INVENTARIO, "w") as f:
        json.dump(inventario, f, indent=2)

def agregar_articulo(inventario):
    """
    Agrega un nuevo artículo al inventario.
    """
    id_articulo = str(uuid.uuid4()) # Genera un UUID como ID único
    descripcion = input("Ingrese la descripción del artículo: ")
    while True:
        cantidad = input("Ingrese la cantidad: ")
        if not funciones.validar_cantidad(cantidad):
            print("La cantidad debe ser un número entero positivo.")
            continue
        cantidad = int(cantidad)
        break

    while True:
        precio_compra = input("Ingrese el precio de compra: ")
        if not funciones.validar_precio_compra(precio_compra):
            print("El precio de compra debe ser un número positivo.")
            continue
        precio_compra = float(precio_compra)
        break

    while True:
        fecha_compra_str = input("Ingrese la fecha de compra (YYYY-MM-DD): ")
        if not funciones.validar_fecha_compra(fecha_compra_str):
            print("Formato de fecha incorrecto. Use YYYY-MM-DD.")
            continue
        fecha_compra = datetime.datetime.strptime(fecha_compra_str, "%Y-%m-%d").date()
        break

    categoria = input("Ingrese la categoría del artículo: ")

    articulo = {
        "id": id_articulo,
        "descripcion": descripcion,
        "cantidad": cantidad,
        "precio_compra": precio_compra,
        "fecha_compra": fecha_compra.strftime("%Y-%m-%d"), # Guarda la fecha como string
        "categoria": categoria
    }

    inventario.append(articulo)
    guardar_inventario(inventario)
    print("Artículo agregado al inventario.")

def listar_articulos(inventario):
    """
    Lista los artículos del inventario.
    """
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n--- INVENTARIO ---")
    for articulo in inventario:
        print(f"ID: {articulo['id']}")
        print(f"Descripción: {articulo['descripcion']}")
        print(f"Cantidad: {articulo['cantidad']}")
        print(f"Precio de Compra: {articulo['precio_compra']}")
        print(f"Fecha de Compra: {articulo['fecha_compra']}")
        print(f"Categoría: {articulo['categoria']}")
        print("-" * 20)

def modificar_articulo(inventario):
    """
    Modifica un artículo existente en el inventario.
    """
    id_articulo = input("Ingrese el ID del artículo que desea modificar: ")
    for articulo in inventario:
        if articulo["id"] == id_articulo:
            print("Artículo encontrado. Ingrese la nueva información (deje en blanco para mantener el valor actual):")

            nueva_descripcion = input(f"Nueva descripción (actual: {articulo['descripcion']}): ") or articulo['descripcion']
            articulo['descripcion'] = nueva_descripcion

            while True:
                nueva_cantidad_str = input(f"Nueva cantidad (actual: {articulo['cantidad']}): ")
                if nueva_cantidad_str == "":
                    break  # Dejar en blanco para mantener el valor actual
                if not funciones.validar_cantidad(nueva_cantidad_str):
                    print("La cantidad debe ser un número entero positivo.")
                    continue
                nueva_cantidad = int(nueva_cantidad_str)
                articulo['cantidad'] = nueva_cantidad
                break

            while True:
                nuevo_precio_compra_str = input(f"Nuevo precio de compra (actual: {articulo['precio_compra']}): ")
                if nuevo_precio_compra_str == "":
                    break  # Dejar en blanco para mantener el valor actual
                if not funciones.validar_precio_compra(nuevo_precio_compra_str):
                    print("El precio de compra debe ser un número positivo.")
                    continue
                nuevo_precio_compra = float(nuevo_precio_compra_str)
                articulo['precio_compra'] = nuevo_precio_compra
                break

            while True:
                nueva_fecha_compra_str = input(f"Nueva fecha de compra (actual: {articulo['fecha_compra']} - YYYY-MM-DD): ")
                if nueva_fecha_compra_str == "":
                    break  # Dejar en blanco para mantener el valor actual
                if not funciones.validar_fecha_compra(nueva_fecha_compra_str):
                    print("Formato de fecha incorrecto. Use YYYY-MM-DD.")
                    continue
                nueva_fecha_compra = datetime.datetime.strptime(nueva_fecha_compra_str, "%Y-%m-%d").date()
                articulo['fecha_compra'] = nueva_fecha_compra.strftime("%Y-%m-%d")
                break

            nueva_categoria = input(f"Nueva categoría (actual: {articulo['categoria']}): ") or articulo['categoria']
            articulo['categoria'] = nueva_categoria

            guardar_inventario(inventario)
            print("Artículo modificado.")
            return

    print("Artículo no encontrado.")

def eliminar_articulo(inventario):
    """
    Elimina un artículo del inventario.
    """
    id_articulo = input("Ingrese el ID del artículo que desea eliminar: ")
    for i, articulo in enumerate(inventario):
        if articulo["id"] == id_articulo:
            del inventario[i]
            guardar_inventario(inventario)
            print("Artículo eliminado.")
            return

    print("Artículo no encontrado.")

def buscar_articulo(inventario):
    """
    Busca artículos en el inventario por descripción o categoría.
    """
    termino_busqueda = input("Ingrese el término de búsqueda (descripción o categoría): ")
    resultados = funciones.buscar_articulos(inventario, termino_busqueda)

    if not resultados:
        print("No se encontraron artículos que coincidan con el término de búsqueda.")
        return

    print("\n--- RESULTADOS DE BÚSQUEDA ---")
    for articulo in resultados:
        print(f"ID: {articulo['id']}")
        print(f"Descripción: {articulo['descripcion']}")
        print(f"Cantidad: {articulo['cantidad']}")
        print(f"Precio de Compra: {articulo['precio_compra']}")
        print(f"Fecha de Compra: {articulo['fecha_compra']}")
        print(f"Categoría: {articulo['categoria']}")
        print("-" * 20)

def mostrar_menu():
    """
    Muestra el menú principal del programa.
    """
    print("\n--- MENÚ ---")
    print("1. Agregar artículo")
    print("2. Listar artículos")
    print("3. Modificar artículo")
    print("4. Eliminar artículo")
    print("5. Buscar artículo")
    print("6. Salir")

def main():
    """
    Función principal del programa.
    """
    inventario = cargar_inventario()

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_articulo(inventario)
        elif opcion == "2":
            listar_articulos(inventario)
        elif opcion == "3":
            modificar_articulo(inventario)
        elif opcion == "4":
            eliminar_articulo(inventario)
        elif opcion == "5":
            buscar_articulo(inventario)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

