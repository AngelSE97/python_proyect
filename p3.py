'''precios_bebida= [('capuchino',1.2),('expresso',1.5),('champu',1.9)]

for bebida,precio in precios_bebida:
    print(bebida,precio)'''

precios_bebida= [('capuchino',1.2),('expresso',2.5),('champu',1.9)]


def mas_caro(lista_p):
    precio_mayor = 0
    bebida_mas_cara = ''

    for bebida, precio in lista_p:
        if precio > precio_mayor:
            precio_mayor = precio
            bebida_mas_cara= bebida
        else:
            pass
    return (precio_mayor,bebida_mas_cara)

print(mas_caro(precios_bebida))