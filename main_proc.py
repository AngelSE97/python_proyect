import utils
from datetime import datetime

def __main__():
    '''
    fecha_devuelta = utils.f_valida_fecha(None, 'MMM DD YYYY HH12:MI PM')
    print ('            SALIDA ===> ',fecha_devuelta)

    fecha_devuelta = utils.f_valida_fecha(None, 'MMM DD YYYY HH12:MI AM')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')



    fecha_devuelta = utils.f_valida_fecha(None, 'YYYY-MM-DD HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)


    fecha_devuelta = utils.f_valida_fecha(None, 'MMM DD YYYY HH12:MI')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha('   null   ', 'DD-MM-YYYY')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha('null ', 'YYYY-MM-DD')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha('null', 'DD/MM/YYYY')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha('28022023', '')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')


    fecha_devuelta = utils.f_valida_fecha(' ', 'YYYY-MM-DD HH24:MI:SS')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')




    fecha_devuelta = utils.f_valida_fecha('28/02/23','DD/MM/YY')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')



    fecha_devuelta = utils.f_valida_fecha('02/28/23', 'MM/DD/YY')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha('Jan 27 2023 12:15 AM', 'MMM DD YYYY HH12:MI AM')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha('Jan 27 2023 12:15 PM', 'MMM DD YYYY HH12:MI PM')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')



    fecha_devuelta = utils.f_valida_fecha('2023-02-15 16:33:52', 'YYYY-MM-DD HH24:MI:SS')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(datetime.strptime('2023/06/27 12:20:23.654321', '%Y/%m/%d %H:%M:%S.%f'), 'YYYY-MM-DD HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(datetime.strptime('27/06/2023', '%d/%m/%Y'), 'YYYY-MM-DD HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(datetime.strptime('13:25:30', '%H:%M:%S'), 'HH24:MI:SS')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(datetime.strptime('02-28-2023', '%m-%d-%Y'), 'DD/MM/YYYY')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(datetime.strptime('02-28-2023 19:20:25', '%m-%d-%Y %H:%M:%S'), 'DD/MM/YYYY')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(datetime.strptime('2023/06/27', '%Y/%m/%d'), 'YYYY-MM-DD HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(datetime.strptime('05-08-2021 19:03:24.585 -1012', '%d-%m-%Y %H:%M:%S.%f %z'), 'DD-MM-YYYY HH24:MI:SS.nnn Z')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(datetime.strptime('05/08/2021 19:03:24.585+1012', '%d/%m/%Y %H:%M:%S.%f%z'), 'DD/MM/YYYY HH24:MI:SS.nnnZ')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(datetime.strptime('2021-08-05 19:03:24.585 -1012', '%Y-%m-%d %H:%M:%S.%f %z'), 'YYYY-MM-DD HH24:MI:SS.nnn Z')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(datetime.strptime('2021/08/05 19:03:24.585+1012', '%Y/%m/%d %H:%M:%S.%f%z'), 'YYYY/MM/DD HH24:MI:SS.nnnZ')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')






    fecha_devuelta = utils.f_valida_fecha('13-de-01-de-2023', 'DD-de-MM-de-YYYY')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(datetime.strptime('02-28-2023', '%m-%d-%Y'), 'MM/DD/YYYY')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')


    fecha_devuelta = utils.f_valida_fecha('13:25:54.123456', 'HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (type(fecha_devuelta))

    fecha_devuelta = utils.f_valida_fecha('05-08-2021 19:03:24.585000 +1012', 'DD-MM-YYYY HH24:MI:SS.nnn Z')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha('05/08/2021 19:03:24.585000+1012', 'DD/MM/YYYY HH24:MI:SS.nnnZ')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha('2021-08-05 10:03:24.585000 +1012', 'YYYY-MM-DD HH24:MI:SS.nnn Z')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha('2021/08/05 10:03:24.585000+1012', 'YYYY/MM/DD HH24:MI:SS.nnnZ')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(datetime.strptime('05-08-2021 19:03:24 -1012', '%d-%m-%Y %H:%M:%S %z'), 'DD-MM-YYYY HH24:MI:SS Z')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(datetime.strptime('05/08/2021 19:03:24+1012', '%d/%m/%Y %H:%M:%S%z'), 'DD/MM/YYYY HH24:MI:SSZ')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(datetime.strptime('2021-08-05 19:03:24 -1012', '%Y-%m-%d %H:%M:%S %z'), 'YYYY-MM-DD HH24:MI:SS Z')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(datetime.strptime('2021/08/05 19:03:24+1012', '%Y/%m/%d %H:%M:%S%z'), 'YYYY/MM/DD HH24:MI:SSZ')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')


    fecha_devuelta = utils.f_valida_fecha('13:25:54.123456', 'HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' ', 'HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' null', 'HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(None,'HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')


    fecha_devuelta = utils.f_valida_fecha('13:25:54', 'HH24:MI:SS')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' ', 'HH24:MI:SS')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' null', 'HH24:MI:SS')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(None, 'HH24:MI:SS')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')


    fecha_devuelta = utils.f_valida_fecha('13:25', 'HH24:MI')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' ', 'HH24:MI')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' null', 'HH24:MI')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(None, 'HH24:MI')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha('2023-05-20 13:25:54.123456', 'YYYY-MM-DD HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' ', 'YYYY-MM-DD HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' null', 'YYYY-MM-DD HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(None, 'YYYY-MM-DD HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')


    fecha_devuelta = utils.f_valida_fecha('2023-05-20 13:25:54', 'YYYY-MM-DD HH24:MI:SS')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' ', 'YYYY-MM-DD HH24:MI:SS')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' null', 'YYYY-MM-DD HH24:MI:SS')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(None, 'YYYY-MM-DD HH24:MI:SS')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')


    fecha_devuelta = utils.f_valida_fecha('2023-05-20 13:25', 'YYYY-MM-DD HH24:MI')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' ', 'YYYY-MM-DD HH24:MI')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' null', 'YYYY-MM-DD HH24:MI')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(None, 'YYYY-MM-DD HH24:MI')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')
    

    fecha_devuelta = utils.f_valida_fecha('2023/05/20 13:25:54.123456', None)
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha('2023/05/20 13:25:54.123456', 'null')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha('2023/05/20 13:25:54.123456', 'YYYY/MM/DD HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' ', 'YYYY/MM/DD HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' null', 'YYYY/MM/DD HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(None, 'YYYY/MM/DD HH24:MI:SS.nnn')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')


    fecha_devuelta = utils.f_valida_fecha('2023/05/20 13:25:54', 'YYYY/MM/DD HH24:MI:SS')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' ', 'YYYY/MM/DD HH24:MI:SS')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' null', 'YYYY/MM/DD HH24:MI:SS')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(None, 'YYYY/MM/DD HH24:MI:SS')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')


    fecha_devuelta = utils.f_valida_fecha('2023/05/20 13:25', 'YYYY/MM/DD HH24:MI')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')
    '''
    fecha_devuelta = utils.f_valida_fecha(' ', 'YYYY/MM/DD HH24:MI')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')

    fecha_devuelta = utils.f_valida_fecha(' null', 'YYYY/MM/DD HH24:MI')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')
    '''
    
    fecha_devuelta = utils.f_valida_fecha(None, 'YYYY/MM/DD HH24:MI')
    print ('            SALIDA ===> ',fecha_devuelta)
    print (' ')
'''

__main__()

