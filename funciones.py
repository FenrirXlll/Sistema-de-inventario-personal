import datetime

def validar_cantidad(cantidad):
    """
    Valida que la cantidad sea un número entero positivo.
    Retorna True si la cantidad es válida, False de lo contrario.
    """
    try:
        cantidad = int(cantidad)
        if cantidad <= 0:
            return False
        return True
    except ValueError:
        return False

def validar_precio_compra(precio_compra):
    """
    Valida que el precio de compra sea un número positivo.
    Retorna True si el precio de compra es válido, False de lo contrario.
    """
    try:
        precio_compra = float(precio_compra)
        if precio_compra <= 0:
            return False
        return True
    except ValueError:
        return False

def validar_fecha_compra(fecha_compra):
    """
    Valida que la fecha de compra tenga el formato YYYY-MM-DD.
    Retorna True si la fecha de compra es válida, False de lo contrario.
    """
    try:
        datetime.datetime.strptime(fecha_compra, "%Y-%m-%d").date()
        return True
    except ValueError:
        return False

def formatear_fecha(fecha):
  """
  Formatea la fecha al formato YYYY-MM-DD
  """
  try:
      fecha_compra = datetime.datetime.strptime(fecha, "%Y-%m-%d").date()
      return fecha_compra.strftime("%Y-%m-%d")
  except ValueError:
      return None

def buscar_articulos(inventario, termino_busqueda):
    """
    Busca artículos en el inventario por descripción o categoría.
    Retorna una lista con los resultados de la búsqueda.
    """
    termino_busqueda = termino_busqueda.lower()
    resultados = []
    for articulo in inventario:
        if termino_busqueda in articulo["descripcion"].lower() or termino_busqueda in articulo["categoria"].lower():
            resultados.append(articulo)
    return resultados
