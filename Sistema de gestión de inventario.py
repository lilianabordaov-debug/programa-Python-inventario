# Sistema de gestión de inventario

# Matriz de artículos
inventario = [
    ["A01", "Teclado", 5, 10],
    ["A02", "Mouse", 15, 10],
    ["A03", "Monitor", 3, 8],
    ["A04", "USB", 20, 15],
    ["A05", "Impresora", 2, 5]
]

# Función para calcular cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Encabezado de tabla
print("=" * 75)
print("{:<10} {:<15} {:<15} {:<15} {:<15}".format(
    "Código", "Artículo", "Stock Actual",
    "Stock Mínimo", "Cantidad Pedir"
))
print("=" * 75)

# Recorrer inventario
for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print("{:<10} {:<15} {:<15} {:<15} {:<15}".format(
        codigo,
        nombre,
        stock_actual,
        stock_minimo,
        cantidad_pedir
    ))

print("=" * 75)