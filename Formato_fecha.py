from datetime import datetime
from dateutil import parser

date_defaults = {
          '%Y-%m-%d %H:%M:%S.%f %z': '9999-01-01 00:00:00.000000 +00:00'
        , '%Y-%m-%d %I:%M %p':       '9999-01-01 00:00 AM'
        , '%Y-%m-%d %H:%M:%S %z':    '9999-01-01 00:00:00 +00:00'
        , '%Y-%m-%d %H:%M:%S.%f':    '9999-01-01 00:00:00.000000'
        , '%Y-%m-%d %H:%M:%S':       '9999-01-01 00:00:00'
        , '%Y-%m-%d':                '9999-01-01'
        , '%Y-%m-%d%H:%M:%S':        '9999-01-01 00:00:00'
        , '%Y-%m-%d %H:%M':          '9999-01-01 00:00'
        , '%H:%M:%S.%f':             '00:00:00.000000'
        , '%H:%M:%S':                '00:00:00'
        , '%H:%M':                   '00:00'
    }
#esta funcion detecta el forato de las fechas y asigna el formato salida
def form_fecha(date_value,formatoint,formato):

    if formatoint is None or formatoint == '' or formatoint == ' ' or formatoint == 'NULL':

        fecha_str = date_value #INGRESAMOS CUALQUIER FORMATO
        fecha = parser.parse(fecha_str)#IDENTIFICA LA FECHA Y EL FORMATO QUE ESTAMOS DEFINIENDO
        # Convierte el objeto de fecha en una cadena de caracteres usando strftime
        nuevo_formato = fecha.strftime(formato)#AQUI SE PONE EL FORMATO DE LA FECHA
        # Convierte el objeto de fecha en datetime.datetime usando strptime
        fec=datetime.strptime(nuevo_formato,formato)
        return nuevo_formato,fec

    else:
        date_value = datetime.strptime(date_value, formatoint)

        fecha_str = date_value  # INGRESAMOS CUALQUIER FORMATO
        # Convierte el objeto de fecha en una cadena de caracteres usando strftime
        nuevo_formato = fecha_str.strftime(formato)
        # Convierte el objeto de fecha en datetime.datetime usando strptime
        fec = datetime.strptime(nuevo_formato, formato)
        return nuevo_formato,fec
#esta funcion asigna valores por defautl si tenemos fechas vacias
def valida_fecha(date_value1,formatoint,formato1):

    if  date_value1.strip().upper() == '' or date_value1.strip().upper() == 'NULL':
        date_value1  = date_defaults[formato1]
        return form_fecha(date_value1,formatoint,formato1)

    elif formato1 == '%H:%M:%S.%f' or formato1 == '%H:%M:%S' or formato1 == '%H:%M':
        return form_fecha(date_value1, formatoint, formato1)

    if formato1 is None or formato1.strip().upper() == ''  or formato1.strip().upper() == 'NULL' :
        formato1 = '%Y-%m-%d %H:%M:%S'
        return form_fecha(date_value1, formatoint,formato1)

    if (date_value1 is None and formato1.strip().upper() == '') or (date_value1.strip().upper() == '' and formato1 is None) or (date_value1.strip().upper() == '' and formato1.strip().upper() == ''):
        date_value1 = '9999-01-01 00:00:00'
        formato1 = '%Y-%m-%d %H:%M:%S'
        return form_fecha(date_value1,formatoint, formato1)

    try:
        return form_fecha(date_value1, formatoint,formato1)

    except ValueError:
        print('Error en formato de fecha. Devuelve None')
        return None
#esta funcion valida si el valor es string o fecha
def valida_tipo_dato(date_value1,formatoint,formato1):

    if date_value1 is None:
        date_value1 = date_defaults[formato1]
        return form_fecha(date_value1, formatoint, formato1)

    if isinstance(date_value1,str):
        return valida_fecha(date_value1,formatoint,formato1)

    if type(date_value1) is datetime:
        date_value1 = date_value1.strftime(formato1)

        return valida_fecha(date_value1,formatoint,formato1)

    else:
         print('Error en formato de fecha. Devuelve None')
         return None

#x=datetime.now()
#el valor de la fecha
#x=datetime.strptime('2021/08/05 19:03:24+1012', '%Y/%m/%d %H:%M:%S%z')
x='28-de-02-de-2023'
#introdiucir el formato cuando la fecha empiece con dia y sean los primeros 12 dias del mes, con el formato %Y-%m-%d %H:%M:%S %p, %d-de-%m-de-%Y,
y ='%d-de-%m-de-%Y'
#formato que le queremos dar en la salida
z ='%Y-%m-%d %H:%M:%S %p'

a,b= valida_tipo_dato(x,y,z)
print(a)
print(type(a))
print(b)
print(type(b))