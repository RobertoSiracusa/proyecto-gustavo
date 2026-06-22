# Maquina Expendedora Prepagada

Simulador de consola de una maquina expendedora que funciona con tarjetas
prepagadas. Maneja un catalogo en forma de matriz, ventas validadas por saldo,
reabastecimiento de inventario y generacion de reportes.

## Autores

- Gustavo Lujan
- George Loutfi
- Fernando Perez

## Requisitos

- Python 3
- matplotlib (opcional, solo para las graficas del reporte). Si no esta
  instalado, el programa funciona igual y omite las graficas.

## Como ejecutar

```
python3 main.py
```

Al iniciar, la maquina carga el inventario local. Si no existe, crea uno por
defecto ya lleno. Luego intenta sincronizar precios y tarjetas con el
repositorio remoto.

## Estructura

```
main.py                          Programa principal y flujos de la interfaz
modelos/
  __init__.py                    Expone las clases del paquete
  producto.py                    Clase Producto
  tarjeta.py                     Clase Tarjeta
  inventario_controlador.py      Persistencia en archivos y sincronizacion
```

Los archivos `productos.txt`, `tarjetas.txt`, `reporte_ventas.txt` y las
imagenes `.png` se generan en tiempo de ejecucion y no se versionan.

## Uso

Desde el menu principal se introduce:

- Una coordenada (por ejemplo `A1`) para comprar un producto.
- `RS` para entrar al menu de Restock (reabastecer o reasignar paneles).
- `RP` para generar el reporte de ventas.
- `SALIR` para apagar la maquina.

### Compra

1. Se selecciona el producto por su coordenada.
2. Se introduce el numero de tarjeta. El numero se convierte a un hash
   SHA-256 y se compara con las tarjetas registradas.
3. Si la tarjeta existe y tiene saldo suficiente, se confirma la compra, se
   descuenta el saldo y se descuenta una unidad del inventario.

### Tarjetas de prueba

Si no existe `tarjetas.txt`, se crean estas tarjetas con su saldo inicial:

| Numero       | Saldo  |
|--------------|--------|
| 1234567890   | 50.00  |
| 9876543210   | 100.00 |
| 1223334444   | 20.00  |
| 4444333221   | 15.50  |
| 1010101010   | 200.00 |

## Reportes

La opcion `RP` genera `reporte_ventas.txt` con el desglose de productos,
total de unidades vendidas, dinero cobrado y consumo por usuario. Si
matplotlib esta disponible, tambien guarda graficas en formato PNG.
