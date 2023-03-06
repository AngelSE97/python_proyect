def una_funcion(funcion):
    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')

    return otra_funcion

@una_funcion
def mayuscula(texto):
    print (texto.upper())

@una_funcion
def minuscula(texto):
    print (texto.lower())



mayuscula('hola world')

