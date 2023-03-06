from datetime import datetime


'''
    Funcion universal de validacion de fechas. Devuelve cadena con formato default establecido
'''
def f_valida_fecha(p_value, p_format):
    # Fechas default
    date_defaults = {
                     '%Y-%m-%d %H:%M:%S.%f %z':     '9999-01-01 00:00:00.000000 +00:00'
                    ,'%Y-%m-%d %I:%M %p':           '9999-01-01 00:00 AM'
                    ,'%Y-%m-%d %H:%M:%S %z':        '9999-01-01 00:00:00 +00:00'
                    ,'%Y-%m-%d %H:%M:%S.%f':        '9999-01-01 00:00:00.000000'
                    ,'%Y-%m-%d %H:%M:%S':           '9999-01-01 00:00:00'
                    ,'%Y-%m-%d':                    '9999-01-01'
                    ,'%Y-%m-%d%H:%M:%S':            '9999-01-01 00:00:00'
                    ,'%Y-%m-%d %H:%M':              '9999-01-01 00:00'
                    ,'%H:%M:%S.%f':                 '00:00:00.000000'
                    ,'%H:%M:%S':                    '00:00:00'
                    ,'%H:%M':                       '00:00'
                    }

    # Formatos de casteo y de salida por formato de fecha de entrada
    date_formats  = {
                     'DD-MM-YY':                    ('%d-%m-%y',                '%Y-%m-%d')
                    ,'DD/MM/YY':                    ('%d/%m/%y',                '%Y-%m-%d')
                    ,'MM-DD-YY':                    ('%m-%d-%y',                '%Y-%m-%d')

                    ,'MM/DD/YY':                    ('%m/%d/%y',                '%Y-%m-%d')
                    ,'YY-MM-DD':                    ('%y-%m-%d',                '%Y-%m-%d')
                    ,'YY/MM/DD':                    ('%y/%m/%d',                '%Y-%m-%d')
                    ,'DDMMYY':                      ('%d%m%y',                  '%Y-%m-%d')
                    ,'MMDDYY':                      ('%m%d%y',                  '%Y-%m-%d')
                    ,'YYMMDD':                      ('%y%m%d',                  '%Y-%m-%d')
                    ,'DD-MM-YYYY':                  ('%d-%m-%Y',                '%Y-%m-%d')
                    ,'DD/MM/YYYY':                  ('%d/%m/%Y',                '%Y-%m-%d')
                    ,'MM-DD-YYYY':                  ('%m-%d-%Y',                '%Y-%m-%d')
                    ,'MM/DD/YYYY':                  ('%m/%d/%Y',                '%Y-%m-%d')
                    ,'YYYY-MM-DD':                  ('%Y-%m-%d',                '%Y-%m-%d')
                    ,'YYYY/MM/DD':                  ('%Y/%m/%d',                '%Y-%m-%d')
                    ,'DDMMYYYY':                    ('%d%m%Y',                  '%Y-%m-%d')
                    ,'MMDDYYYY':                    ('%m%d%Y',                  '%Y-%m-%d')
                    ,'YYYYMMDD':                    ('%Y%m%d',                  '%Y-%m-%d')

                    ,'DD/MMM/YYYY':                 ('%d/%b/%Y',                '%Y-%m-%d')
                    ,'DDMMMYY':                     ('%d%b%y',                  '%Y-%m-%d')
                    ,'DD-MMM-YY':                   ('%d-%b-%y',                '%Y-%m-%d') #se modifico el formato, tenia / en vez de -
                    ,'DD/MMM/YY':                   ('%d/%b/%y',                '%Y-%m-%d') #se agrega formato DD/MMM/YY
                    ,'DD-MMM-YYYY':                 ('%d-%b-%Y',                '%Y-%m-%d')

                    ,'DD MMM YY':                   ('%d %b %y',                '%Y-%m-%d')# se agrega formato DD MMM YY
                    ,'DD MMM YYYY':                 ('%d %b %Y',                '%Y-%m-%d')# se agrega formato DD MMM YYYY
                    ,'DD MMM YY HH24:MI:SS':        ('%d %b %y %H:%M:%S',       '%Y-%m-%d %H:%M:%S')# se agrega formato DD MMM YY  %H:%M:%S
                    ,'DD MMM YYYY HH24:MI:SS':      ('%d %b %Y %H:%M:%S',       '%Y-%m-%d %H:%M:%S')# se agrega formato DD MMM YYYY  %H:%M:%S
                    ,'DD MMM YY HH24:MI:SS.nnn':    ('%d %b %y %H:%M:%S.%f',    '%Y-%m-%d %H:%M:%S')# se agrega formato
                    ,'DD MMM YYYY HH24:MI:SS.nnn':  ('%d %b %Y %H:%M:%S.%f',    '%Y-%m-%d %H:%M:%S')# se agrega formato

                    ,'DD MM YY':                    ('%d %m %y',                '%Y-%m-%d')# se agrega formato
                    ,'DD MM YYYY':                  ('%d %m %Y',                '%Y-%m-%d')# se agrega formato
                    ,'DD MM YY HH24:MI:SS':         ('%d %m %y %H:%M:%S',       '%Y-%m-%d %H:%M:%S')# se agrega formato
                    ,'DD MM YYYY HH24:MI:SS':       ('%d %m %Y %H:%M:%S',       '%Y-%m-%d %H:%M:%S')# se agrega formato
                    ,'DD MM YY HH24:MI:SS.nnn':     ('%d %m %y %H:%M:%S.%f',    '%Y-%m-%d %H:%M:%S')# se agrega formato
                    ,'DD MM YYYY HH24:MI:SS.nnn':   ('%d %m %Y %H:%M:%S.%f',    '%Y-%m-%d %H:%M:%S')# se agrega formato

                    ,'YYYY-MM-DD HH24:MI:SS.nnn':   ('%Y-%m-%d %H:%M:%S.%f',    '%Y-%m-%d %H:%M:%S.%f')
                    ,'YYYY-MM-DD HH24:MI:SS':       ('%Y-%m-%d %H:%M:%S',       '%Y-%m-%d %H:%M:%S')
                    ,'YYYY-MM-DD HH24:MI':          ('%Y-%m-%d %H:%M',          '%Y-%m-%d %H:%M')
                    ,'YYYY/MM/DD HH24:MI:SS.nnn':   ('%Y/%m/%d %H:%M:%S.%f',    '%Y-%m-%d %H:%M:%S.%f')
                    ,'YYYY-MM-DD HH24:MI:SS PM':    ('%Y-%m-%d %H:%M:%S %p',    '%Y-%m-%d %H:%M:%S %p')
                    ,'YYYY/MM/DD HH24:MI:SS':       ('%Y/%m/%d %H:%M:%S',       '%Y-%m-%d %H:%M:%S')
                    ,'YYYY/MM/DD HH24:MI':          ('%Y/%m/%d %H:%M',          '%Y-%m-%d %H:%M')
                    ,'HH24:MI:SS.nnn':              ('%H:%M:%S.%f',             '%H:%M:%S.%f')#con 1 valor del milisegundo se puede ingresar la fecha, y hasta 6 valores despues del punto
                    ,'HH24:MI:SS':                  ('%H:%M:%S',                '%H:%M:%S')
                    ,'HH24:MI':                     ('%H:%M',                   '%H:%M')#se tomaria el valor de val_value para tener una fecha valida y no solo horas y min?
                    ,'YYYYMMDD HH24:MI:SS.nnn':     ('%Y%m%d %H:%M:%S.%f',      '%Y-%m-%d %H:%M:%S.%f')#se puede tener un vaslor con y,m,d y que se aomplete con H,M,S.n?
                    ,'YYYYMMDD HH24:MI:SS':         ('%Y%m%d %H:%M:%S',         '%Y-%m-%d %H:%M:%S')
                    ,'YYYYMMDD HH24:MI':            ('%Y%m%d %H:%M',            '%Y-%m-%d %H:%M')
                    ,'YYYYMMDDHH24:MI:SS':          ('%Y%m%d%H:%M:%S',          '%Y-%m-%d%H:%M:%S')
                    ,'YYYYMMDDHH24:MI:SS.nnn':      ('%Y%m%d%H:%M:%S.%f',       '%Y-%m-%d%H:%M:%S')#se agregan los miliseg al formato '%Y%m%d%H:%M:%S'
                    ,'YYYYMMDDHH24:MI':             ('%Y%m%d%H:%M:%S',          '%Y-%m-%d%H:%M:%S')#se quitan los miliseg y los seg al formato '%Y%m%d%H:%M:%S.%f'
                    ,'DD/MM/YYYY HH24:MI:SS.nnn':   ('%d/%m/%Y %H:%M:%S.%f',    '%Y-%m-%d %H:%M:%S.%f')
                    ,'DD/MM/YYYY HH24:MI:SS':       ('%d/%m/%Y %H:%M:%S',       '%Y-%m-%d %H:%M:%S')
                    ,'DD/MM/YYYY HH24:MI':          ('%d/%m/%Y %H:%M',          '%Y-%m-%d %H:%M')
                    ,'MM/DD/YYYY HH24:MI':          ('%m/%d/%Y %H:%M',          '%Y-%m-%d %H:%M')#se agrega el formato 'MM/DD/YYYY HH24:MI'
                    ,'MM/DD/YYYY HH24:MI:SS.nnn':   ('%m/%d/%Y %H:%M:%S.%f',    '%Y-%m-%d %H:%M:%S.%f')#se agrega el formato 'MM/DD/YYYY HH24:MI:SS.nnn'
                    ,'MM/DD/YYYY HH24:MI:SS':       ('%m/%d/%Y %H:%M:%S',       '%Y-%m-%d %H:%M:%S')#se agrega el formato 'MM/DD/YYYY HH24:MI:SS'

                    ,'DD-MM-YYYY HH24:MI:SS.nnn':   ('%d-%m-%Y %H:%M:%S.%f',    '%Y-%m-%d %H:%M:%S.%f')# se agregan formato
                    ,'DD-MM-YYYY HH24:MI:SS':       ('%d-%m-%Y %H:%M:%S',       '%Y-%m-%d %H:%M:%S')
                    ,'DD-MM-YYYY HH24:MI':          ('%d-%m-%Y %H:%M',          '%Y-%m-%d %H:%M')
                    ,'MM-DD-YYYY HH24:MI':          ('%m-%d-%Y %H:%M',          '%Y-%m-%d %H:%M')
                    ,'MM-DD-YYYY HH24:MI:SS.nnn':   ('%m-%d-%Y %H:%M:%S.%f',    '%Y-%m-%d %H:%M:%S.%f')
                    ,'MM-DD-YYYY HH24:MI:SS':       ('%m-%d-%Y %H:%M:%S',       '%Y-%m-%d %H:%M:%S')

                    ,'MMM DD YYYY HH12:MI':         ('%b %d %Y %I:%M',          '%Y-%m-%d %I:%M %p')#se agrega formato
                    ,'MM DD YYYY HH12:MI AM':       ('%m %d %Y %I:%M %p',       '%Y-%m-%d %I:%M %p')#se agrega formato
                    ,'MM DD YYYY HH12:MI PM':       ('%m %d %Y %I:%M %p',       '%Y-%m-%d %I:%M %p')#se agrega formato
                    ,'DD MM YYYY HH12:MI AM':       ('%d %m %Y %I:%M %p',       '%Y-%m-%d %I:%M %p')#se agrega formato
                    ,'DD MM YYYY HH12:MI PM':       ('%d %m %Y %I:%M %p',       '%Y-%m-%d %I:%M %p')#se agrega formato
                    ,'MMM DD YYYY HH12:MI AM':      ('%b %d %Y %I:%M %p',       '%Y-%m-%d %I:%M %p')
                    ,'MMM DD YYYY HH12:MI PM':      ('%b %d %Y %I:%M %p',       '%Y-%m-%d %I:%M %p')


                    ,'DD-de-MM-de-YYYY':            ('%d-de-%m-de-%Y',          '%Y-%m-%d')
                    ,'DD de MM de YYYY':            ('%d de %m de %Y',          '%Y-%m-%d')#se agrega el formato 'DD de MM de YYYY'

                    ,'YYYY-MM-DD HH24:MI:SS.nnn Z': ('%Y-%m-%d %H:%M:%S.%f %z', '%Y-%m-%d %H:%M:%S.%f %z')
                    ,'YYYY-MMM-DD HH24:MI:SS.nnn Z':('%Y-%b-%d %H:%M:%S.%f %z', '%Y-%m-%d %H:%M:%S.%f %z')#se agrega formato
                    ,'YYYY-MM-DD HH24:MI:SS.nnnZ':  ('%Y-%m-%d %H:%M:%S.%f%z',  '%Y-%m-%d %H:%M:%S.%f %z')
                    ,'YYYY-MMM-DD HH24:MI:SS.nnnZ': ('%Y-%b-%d %H:%M:%S.%f%z',  '%Y-%m-%d %H:%M:%S.%f %z')#se agrega formato
                    ,'YYYY/MM/DD HH24:MI:SS.nnn Z': ('%Y/%m/%d %H:%M:%S.%f %z', '%Y-%m-%d %H:%M:%S.%f %z')
                    ,'YYYY/MMM/DD HH24:MI:SS.nnn Z':('%Y/%b/%d %H:%M:%S.%f %z', '%Y-%m-%d %H:%M:%S.%f %z')#se agrega formato
                    ,'YYYY/MM/DD HH24:MI:SS.nnnZ':  ('%Y/%m/%d %H:%M:%S.%f%z',  '%Y-%m-%d %H:%M:%S.%f %z')
                    ,'YYYY/MMM/DD HH24:MI:SS.nnnZ': ('%Y/%b/%d %H:%M:%S.%f%z',  '%Y-%m-%d %H:%M:%S.%f %z')#se agrega formato
                    ,'DD-MM-YYYY HH24:MI:SS.nnn Z': ('%d-%m-%Y %H:%M:%S.%f %z', '%Y-%m-%d %H:%M:%S.%f %z')
                    ,'DD-MMM-YYYY HH24:MI:SS.nnn Z':('%d-%b-%Y %H:%M:%S.%f %z', '%Y-%m-%d %H:%M:%S.%f %z')#se agrega formato
                    ,'DD-MM-YYYY HH24:MI:SS.nnnZ':  ('%d-%m-%Y %H:%M:%S.%f%z',  '%Y-%m-%d %H:%M:%S.%f %z')
                    ,'DD-MMM-YYYY HH24:MI:SS.nnnZ': ('%d-%b-%Y %H:%M:%S.%f%z',  '%Y-%m-%d %H:%M:%S.%f %z')#se agrega formato
                    ,'DD/MM/YYYY HH24:MI:SS.nnn Z': ('%d/%m/%Y %H:%M:%S.%f %z', '%Y-%m-%d %H:%M:%S.%f %z')
                    ,'DD/MMM/YYYY HH24:MI:SS.nnn Z':('%d/%b/%Y %H:%M:%S.%f %z', '%Y-%m-%d %H:%M:%S.%f %z')#se agrega formato
                    ,'DD/MM/YYYY HH24:MI:SS.nnnZ':  ('%d/%m/%Y %H:%M:%S.%f%z',  '%Y-%m-%d %H:%M:%S.%f %z')
                    ,'DD/MMM/YYYY HH24:MI:SS.nnnZ': ('%d/%b/%Y %H:%M:%S.%f%z',  '%Y-%m-%d %H:%M:%S.%f %z')#se agrega formato
                    ,'YYYY-MM-DD HH24:MI:SS Z':     ('%Y-%m-%d %H:%M:%S %z',    '%Y-%m-%d %H:%M:%S %z')
                    ,'YYYY-MMM-DD HH24:MI:SS Z':    ('%Y-%b-%d %H:%M:%S %z',    '%Y-%m-%d %H:%M:%S %z')#se agrega formato
                    ,'YYYY-MM-DD HH24:MI:SSZ':      ('%Y-%m-%d %H:%M:%S%z',     '%Y-%m-%d %H:%M:%S %z')
                    ,'YYYY-MMM-DD HH24:MI:SSZ':     ('%Y-%b-%d %H:%M:%S%z',     '%Y-%m-%d %H:%M:%S %z')#se agrega formato
                    ,'YYYY/MM/DD HH24:MI:SS Z':     ('%Y/%m/%d %H:%M:%S %z',    '%Y-%m-%d %H:%M:%S %z')
                    ,'YYYY/MMM/DD HH24:MI:SS Z':    ('%Y/%b/%d %H:%M:%S %z',    '%Y-%m-%d %H:%M:%S %z')#se agrega formato
                    ,'YYYY/MM/DD HH24:MI:SSZ':      ('%Y/%m/%d %H:%M:%S%z',     '%Y-%m-%d %H:%M:%S %z')
                    ,'YYYY/MMM/DD HH24:MI:SSZ':     ('%Y/%b/%d %H:%M:%S%z',     '%Y-%m-%d %H:%M:%S %z')#se agrega formato
                    ,'DD-MM-YYYY HH24:MI:SS Z':     ('%d-%m-%Y %H:%M:%S %z',    '%Y-%m-%d %H:%M:%S %z')
                    ,'DD-MMM-YYYY HH24:MI:SS Z':    ('%d-%b-%Y %H:%M:%S %z',    '%Y-%m-%d %H:%M:%S %z')#se agrega formato
                    ,'DD-MM-YYYY HH24:MI:SSZ':      ('%d-%m-%Y %H:%M:%S%z',     '%Y-%m-%d %H:%M:%S %z')
                    ,'DD-MMM-YYYY HH24:MI:SSZ':     ('%d-%b-%Y %H:%M:%S%z',     '%Y-%m-%d %H:%M:%S %z')#se agrega formato
                    ,'DD/MM/YYYY HH24:MI:SS Z':     ('%d/%m/%Y %H:%M:%S %z',    '%Y-%m-%d %H:%M:%S %z')
                    ,'DD/MMM/YYYY HH24:MI:SS Z':    ('%d/%b/%Y %H:%M:%S %z',    '%Y-%m-%d %H:%M:%S %z')#se agrega formato
                    ,'DD/MM/YYYY HH24:MI:SSZ':      ('%d/%m/%Y %H:%M:%S%z',     '%Y-%m-%d %H:%M:%S %z')
                    ,'DD/MMM/YYYY HH24:MI:SSZ':     ('%d/%b/%Y %H:%M:%S%z',     '%Y-%m-%d %H:%M:%S %z')#se agrega formato
                   }


    date_format  = None
    date_default = None


    print ('============================')
    print ('===> p_value =', p_value, '===> TYPE =', type(p_value))
    print ('============================')

    # Si no se recibio el parametro p_format devuelve None
    if p_format is None:
        print ('p_format es None. Formato no valido')
        return None


    # Recupera formatos de fecha y fecha default a partir de p_format
    try:
        print ('Formato valor  = ',p_format)

        date_format  = date_formats[p_format]
        date_default = date_defaults[date_format[1]]

        print ('Formato casteo-date_format[0] = ',date_format[0])
        print ('Formato salida-date_format[1] = ',date_format[1])
    
    except KeyError as ke:
        print ('NO EXISTE INF RN DICCIONARIO. Devuelve None')
        return None


    # Valida si el parametro p_value es None, de ser asi devuelve fecha default para el p_format indicado
    if p_value is None:
        print ('p_value es None. Devuelve formato default')
        return date_default


    # Para manejo de parametro p_value como string
    if isinstance(p_value, str):

        # Si p_value es NULL, null o vacio devuelve fecha default para el p_format indicado
        if p_value.strip().upper() == 'NULL' or p_value.strip().upper() == "":
            print ('p_value es NULL o vacio. Devuelve formato default')
            return date_default

        # Valida fecha (p_value) y devuelve en formato de salida
        try:
            val_value   = datetime.strptime(p_value, date_format[0])
            print ('val_value = ',val_value)
            date_salida = datetime.strptime(p_value, date_format[0]).strftime(date_format[1])
            print ('date_salida = ',date_salida)
            return date_salida

        except ValueError:
            print ('Error en formato de fecha (STR). Devuelve None')
            return None


    # Para manejo de parametro p_value como datetime
    if type(p_value) is datetime:

        # Valida fecha (p_value) y devuelve en formato de salida
        try:
            val_value   = p_value.strftime(date_format[0])
            print ('val_value = ',val_value)
            date_salida = p_value.strftime(date_format[1])
            print ('date_salida = ',date_salida)
            return date_salida
            
        except ValueError:
            print ('Error en formato de fecha. Devuelve None')
            return None

fecha_devuelta = f_valida_fecha('2023/05/20 13:25:54.123456', None)
print ('            SALIDA ===> ',fecha_devuelta)