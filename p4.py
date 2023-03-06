from random import shuffle
palito= ['-','--','---','----']

def mezcla(lista):
    shuffle(lista)
    return lista

def probar():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input('Elige un numero del 1 al 4: ')

    return int(intento)

def checar(lista,intento):
    if lista [intento - 1 ] == '-':
        print('A lavar los platos')
    else:
        print('Te salvaste')

    print(f"te ha tocado {lista[intento - 1]}")


palo_mezclado = mezcla(palito)
seleccion = probar()
checar(palo_mezclado,seleccion)
