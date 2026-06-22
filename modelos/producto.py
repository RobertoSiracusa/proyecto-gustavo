"""
Modelo Producto - Proyecto Maquina Expendedora
Autores: Gustavo Lujan, George Loutfi, Fernando Perez
"""


class Producto:
    """
    Clase que representa un producto individual en la maquina expendedora.
    """
    def __init__(self, codigo, nombre, cantidad, despedida, precio=0.0):
        self.codigo = codigo          # Codigo de 5 letras (ej. CocaC)
        self.nombre = nombre          # Nombre completo para confirmacion
        self.cantidad = int(cantidad)  # Cantidad disponible en stock
        self.despedida = despedida    # Mensaje de despedida personalizado
        self.precio = float(precio)    # Precio, se actualizara con la API

    def actualizar_stock(self, nueva_cantidad):
        """Actualiza la cantidad disponible del producto."""
        self.cantidad = int(nueva_cantidad)
