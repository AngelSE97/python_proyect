from dateutil import parser

def mes_dia(fecha_str2,formato2):
    meses = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    day= int(fecha_str2[:2])

    if day < 13:
        print('hello')

        if formato2.startswith('%d/%m/%y') or formato2.startswith('%d-%m-%y') or formato2.startswith('%d/%m/%Y') or formato2.startswith('%d-%m-%Y'):

            numero_mes = int(fecha_str2[3:5]) - 1
            mes = meses[numero_mes]
            fecha_str2 = fecha_str2[:3] + mes + fecha_str2[5:]

        elif formato2.startswith('%d%m%y'):
            numero_mes = int(fecha_str2[2:4]) - 1
            mes = meses[numero_mes]
            fecha_str2 = fecha_str2[:2] + mes + fecha_str2[4:]

    else :
        return fecha_str2,formato2


    return fecha_str2,formato2






a='13/02/2021'
b='%d/%m/%Y'
x,y= mes_dia(a,b)

print(x)
print(type(x))


'''
fecha = parser.parse(fecha_str)

nuevo_formato = fecha.strftime('%d-%m-%y')
print(nuevo_formato)
print(fecha)

#('%d/%m/%y','%d-%m-%y','%d%m%y','%d-de-%m-de-%Y','%d-%m-%Y %H:%M:%S.%f %z','%d-%m-%Y %H:%M:%S.%f%z','%d/%m/%Y %H:%M:%S.%f %z','%d/%m/%Y %H:%M:%S.%f%z,'%d-%m-%Y %H:%M:%S %z','%d-%m-%Y %H:%M:%S%z','%d/%m/%Y %H:%M:%S %z','%d/%m/%Y %H:%M:%S%z')


fecha_str = '010121'
meses = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
numero_mes = int(fecha_str[2:4]) - 1
mes = meses[numero_mes]
fecha_str = fecha_str[:2] + mes + fecha_str[4:]

print (fecha_str)

'''