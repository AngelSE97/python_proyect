from datetime import datetime
from dateutil import parser

def form_fecha(date_value,formato):

    fecha_str = date_value #INGRESAMOS CUALQUIER FORMATO
    fecha = parser.parse(fecha_str)#IDENTIFICA LA FECHA Y EL FORMATO QUE ESTAMOS DEFINIENDO
    # Convierte el objeto de fecha en una cadena de caracteres usando strftime
    nuevo_formato = fecha.strftime(formato)#AQUI SE PONE EL FORMATO DE LA FECHA
    # Convierte el objeto de fecha en datetime.datetime usando strptime
    fec=datetime.strptime(nuevo_formato,formato)
    return nuevo_formato,fec

def valida_dia(fecha_str2,formato2):
    meses = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    day= int(fecha_str2[:2])

    if day < 13:

        if formato2.startswith('%d/%m/%y') or formato2.startswith('%d-%m-%y') or formato2.startswith('%d/%m/%Y') or formato2.startswith('%d-%m-%Y') or formato2.startswith('%d %m %Y'):

            numero_mes = int(fecha_str2[3:5]) - 1
            mes = meses[numero_mes]
            fecha_str2 = fecha_str2[:3] + mes + fecha_str2[5:]
            return form_fecha(fecha_str2, formato2)

        elif formato2.startswith('%d%m%y'):
            numero_mes = int(fecha_str2[2:4]) - 1
            mes = meses[numero_mes]
            fecha_str2 = fecha_str2[:2] + mes + fecha_str2[4:]
            return form_fecha(fecha_str2, formato2)
    else :
        return form_fecha(fecha_str2,formato2)

def valida_fecha(date_value1,formato1):

    '''if date_value1 is None or date_value1 == '' or date_value1 == ' ' or date_value1 == 'NULL':
        date_value1 = '9999-01-01 00:00:00'
        formato1 = '%Y-%m-%d %H:%M:%S'
        return form_fecha(date_value1, formato1)

    if formato1 is None or formato1 == '' or formato1 == ' ' or formato1 == 'NULL':
        #date_value1 = '9999-01-01 00:00:00'
        formato1 = '%Y-%m-%d %H:%M:%S'
        return form_fecha(date_value1, formato1)'''

    if (date_value1 is None and formato1 == '') or (date_value1 == '' and formato1 is None) or (date_value1 == '' and formato1 == ''):
        date_value1 = '9999-01-01 00:00:00'
        formato1 = '%Y-%m-%d %H:%M:%S'
        return form_fecha(date_value1, formato1)

    try:
        return valida_dia(date_value1, formato1)

    except ValueError:
        print('Error en formato de fecha. Devuelve None')
        return None


'''

#x=None
x='Jan 27 2023 13:15:02 +1012'
#x='28/02/2021'
#x="2023/05/20 13:25:54.123456"
#y=' '
y='%Y-%m-%d %H:%M:%S %z'
#y='%Y-%m-%d %H:%M:%S'
#y='%Y/%m/%d %H:%M:%S.%f'
'''

w ='02 28 23'
r ='%Y-%m-%d %H:%M:%S'
a,b= valida_fecha(w,r)
print(a)
print(type(a))
print(b)
print(type(b))


