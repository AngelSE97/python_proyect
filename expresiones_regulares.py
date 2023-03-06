
import re
texto = 'si necesitas ayuda llama al 015-559-1134 las 24 horas para ayuda'

#palabra = r'\d\d\d-\d\d\d-\d\d\d\d'

#palabra = r'\d{3}-\d{3}-\d{4}'

#palabra = re.compile(r'(\d{3})-(\d{3})-(\d{4})')


resultado = re.search(r'si|horas',texto)

print(resultado)

#busqueda= re.search(palabra,texto)

'''for a in re.finditer(palabra,texto):

    print(a.span())'''

Práctica
Módulo
RE
1

import expresiones_regulares

import expresiones_regulares


def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = expresiones_regulares.search(patron, email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


Práctica
Módulo
RE
2

import expresiones_regulares


def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = expresiones_regulares.search(patron, frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")


Práctica
Módulo
RE
3

import expresiones_regulares


def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")





