"""
Paquete modelos - Proyecto Maquina Expendedora
Expone las clases del dominio para importarlas directamente desde 'modelos'.
"""
from .producto import Producto
from .tarjeta import Tarjeta
from .inventario_controlador import InventarioControlador

__all__ = ["Producto", "Tarjeta", "InventarioControlador"]
