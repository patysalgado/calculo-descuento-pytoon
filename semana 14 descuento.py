def calcular_iva(valor_compra, porcentaje_iva = 12):
    valor_iva = (valor_compra * porcentaje_iva) / 100
    return valor_iva


producto_01 = 127
producto_02 = 747
producto_03 = 55
valor_productos = producto_01 + producto_02 + producto_03
valor_iva = calcular_iva(valor_productos, 15)
valor_total = valor_productos + valor_iva
print(f'Valor total: {valor_total}. Valor productos: {valor_productos}. Valor IVA: {valor_iva}')