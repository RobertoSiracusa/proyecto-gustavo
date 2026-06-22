"""
Modelo Tarjeta - Proyecto Maquina Expendedora
Autores: Gustavo Lujan, George Loutfi, Fernando Perez
"""


class Tarjeta:
    """
    Clase que representa una tarjeta prepagada registrada en el sistema.
    """
    def __init__(self, hashed_numero, saldo):
        self.hashed_numero = hashed_numero  # El hash SHA-256 del numero
        self.saldo = float(saldo)

    def descontar_saldo(self, monto):
        """Descuenta el monto del saldo si es suficiente. Retorna True si se logro."""
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        return False
