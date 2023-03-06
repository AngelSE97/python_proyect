fecha_str = '05-08-2021 19:03:24 -1012'
#'01-01-21'
formato1='%d-%m-%Y %H:%M:%S %z'
#'%d-%m-%Y'

if formato1.startswith('%d/%m/%y') or formato1.startswith('%d-%m-%y') or formato1.startswith('%d/%m/%Y') or formato1.startswith('%d-%m-%Y'):

    meses = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    numero_mes = int(fecha_str[3:5]) - 1
    mes = meses[numero_mes]
    fecha_str = fecha_str[:3] + mes + fecha_str[5:]

elif formato1.startswith('%d%m%y'):

    meses = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    numero_mes = int(fecha_str[2:4]) - 1
    mes = meses[numero_mes]
    fecha_str = fecha_str[:2] + mes + fecha_str[4:]

print(fecha_str)
#return fecha_str,formato1
