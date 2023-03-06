from datetime import datetime
from dateutil import parser
import pytz

'''
'YYYY-MM-DD
YYYY/MM/DD
DD-MM-YYYY
DD/MM/YYYY
MM/DD/YYYY
MM-DD-YYYY
DD.MM.YYYY
DD MMM YYYY (ej. 31 Jan 2023)
DD MMMM YYYY (ej. 31 January 2023)
DD Mon YYYY (ej. 31 Jan 2023)
Mon DD YYYY (ej. Jan 31 2023)
MMM DD YYYY (ej. Jan 31 2023)
MMMM DD YYYY (ej. January 31 2023)
YYYY MMM DD (ej. 2023 Jan 31)
YYYY MMMM DD (ej. 2023 January 31)'''
'2023-01-31 18:20:15 UTC +0000'

fecha_str = '05-08-2021 19:03:24' #INGRESAMOS CUALQUIER FORMATO
fecha = parser.parse(fecha_str)#IDENTIFICA LA FECHA Y EL FORMATO QUE ESTAMOS DEFINIENDO

# Convierte el objeto de fecha en una cadena de caracteres usando strftime
nuevo_formato = fecha.strftime('%d-%m-%Y %H:%M:%S')#AQUI SE PONE EL FORMATO DE LA FECHA
fec=datetime.strptime(nuevo_formato,'%d-%m-%Y %H:%M:%S')

print(fecha)

print(nuevo_formato)
print(type(nuevo_formato))

print(fec)
print(type(fec))
