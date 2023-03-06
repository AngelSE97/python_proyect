'''import datetime
from datetime import date, time, datetime


class DateQuality:
    @staticmethod  # Mas grande que
    def dateLargerThan(newDate, oldDate):
        return newDate > oldDate

    @staticmethod  # Mas chica que
    def dateSmallerThan(newDate, oldDate):
        return newDate < oldDate

    @staticmethod  # Cambiar el formato de fecha
    def changeFormatDate(date):
        # Si es de string a date                  aqui depende como venga el string
        return datetime.datetime.strptime(date, "%d/%m/%Y").date()

        # Se es de date a string  / aqui igual depende como queramos mostrar la fecha en string
        # return date.strftime('%Y-%m-%d')

    @staticmethod  # Horas
    def hasHours(fecha):
        try:
            return fecha.time()
            # return fecha.strftime('%H:%M:%S') #Pendiente
        except:
            return False

    @staticmethod  # Zona horaria
    def hasTimeZone(fecha):
        try:
            return fecha.tzname()
        except:
            return False


date1 = date(2017,6,23)
#date2 = datetime.datetime(1998,4,19)
date3 = '20/01/2023'

print(date1.tzname())
#print(date2)
'''

from datetime import datetime



from datetime import datetime

def is_valid_date(date_string):
    formats = ['%d/%m/%Y', '%Y-%m-%d']
    for date_format in formats:
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            pass
    return False

print(is_valid_date('25/12/2022')) # True
print(is_valid_date("2022-12-25")) # True
print(is_valid_date("32/12/2022")) # False


