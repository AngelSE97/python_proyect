
from datetime import datetime

def is_valid_date(date_string):

    '''date_formats = {
        'DD-MM-YY': ('%d-%m-%y', '%Y-%m-%d')
        , 'DD-MM-YYYY': ('%d-%m-%Y', '%Y-%m-%d')
        , 'DD/MM/YY': ('%d/%m/%y', '%Y-%m-%d')
        , 'DD/MM/YYYY': ('%d/%m/%Y', '%Y-%m-%d')
        , 'DD/MMM/YYYY': ('%d/%b/%Y', '%Y-%m-%d')
        , 'DDMMYY': ('%d%m%y', '%Y-%m-%d')
        , 'DDMMYYYY': ('%d%m%Y', '%Y-%m-%d')
        , 'DDMMMYY': ('%d%b%y', '%Y-%m-%d')
        , 'MM-DD-YY': ('%m-%d-%y', '%Y-%m-%d')
        , 'MM-DD-YYYY': ('%m-%d-%Y', '%Y-%m-%d')
        , 'MM/DD/YY': ('%m/%d/%y', '%Y-%m-%d')
        , 'MM/DD/YYYY': ('%m/%d/%Y', '%Y-%m-%d')
        , 'MMDDYY': ('%m%d%y', '%Y-%m-%d')
        , 'MMDDYYYY': ('%m%d%Y', '%Y-%m-%d')
        , 'YY-MM-DD': ('%y-%m-%d', '%Y-%m-%d')
        , 'YY/MM/DD': ('%y/%m/%d', '%Y-%m-%d')
        , 'YYMMDD': ('%y%m%d', '%Y-%m-%d')
        , 'YYYY-MM-DD': ('%Y-%m-%d', '%Y-%m-%d')
        , 'YYYY/MM/DD': ('%Y/%m/%d', '%Y-%m-%d')
        , 'YYYYMMDD': ('%Y%m%d', '%Y-%m-%d')
        , 'YYYY-MM-DD HH24:MI:SS.nnn': ('%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%d %H:%M:%S.%f')
        , 'YYYYMMDD HH24:MI:SS.nnn': ('%Y%m%d %H:%M:%S.%f', '%Y-%m-%d %H:%M:%S.%f')
        , 'YYYY-MM-DD HH24:MI:SS': ('%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M:%S')
        , 'YYYY/MM/DD HH24:MI:SS': ('%Y/%m/%d %H:%M:%S', '%Y-%m-%d %H:%M:%S')
        , 'YYYYMMDD HH24:MI:SS': ('%Y%m%d %H:%M:%S', '%Y-%m-%d %H:%M:%S')
        , 'YYYYMMDDHH24:MI:SS': ('%Y%m%d%H:%M:%S', '%Y-%m-%d%H:%M:%S')
        , 'DD/MM/YYYY HH24:MI:SS': ('%d/%m/%Y %H:%M:%S', '%Y-%m-%d %H:%M:%S')
        , 'DD-MMM-YY': ('%d/%b/%y', '%Y-%m-%d')
        , 'DD-MMM-YYYY': ('%d-%b-%Y', '%Y-%m-%d')
        , 'HH24:MI:SS': ('%H:%M:%S', '%H:%M:%S')
        , 'MMM DD YYYY HH12:MI AM': ('%b %d %Y %I:%M %p', '%Y-%m-%d %I:%M %p')
        , 'MMM DD YYYY HH12:MI PM': ('%b %d %Y %I:%M %p', '%Y-%m-%d %I:%M %p')
        , 'DD-de-MM-de-YYYY': ('%d-de-%m-de-%Y', '%Y-%m-%d')
    }
'''
   # formats = list(date_formats.items())
    date_formats = ['%d-%m-%y','%Y-%m-%d','%m-%d-%y']

    for date_format in date_formats:
        try:
            datetime.strptime(date_string,date_format)
            return True
        except ValueError:
            pass
    return False


print(is_valid_date('02-12-22')) # True
#print(is_valid_date("2022-12-25")) # True
#print(is_valid_date("32/12/2022")) # False



