'''
import pytz
import datetime

# Obtén la hora actual en la zona horaria de Nueva York
ny_timezone = pytz.timezone("America/Mexico_City")
ny_datetime = datetime.datetime.now(tz=ny_timezone)

# Convierte a la zona horaria de Tokio
tokyo_timezone = pytz.timezone("Asia/Tokyo")
tokyo_datetime = ny_datetime.astimezone(tokyo_timezone)

print(ny_datetime)
print(tokyo_datetime)
'''

import pytz
import datetime
# Especifica la fecha y hora que quieres utilizar
date_input1 = "2023-02-03 12:30"
# Especifica el formato de la fecha y hora de entrada
date_format = "%Y-%m-%d %H:%M"
# Convierte la fecha y hora de entrada a un objeto datetime
parsed_date = datetime.datetime.strptime(date_input1, date_format)
# Obtén la zona horaria de la Ciudad de México
mexico_city_timezone = pytz.timezone("America/Mexico_City")
# Asigna la zona horaria a la fecha y hora especificadas
mexico_city_datetime = mexico_city_timezone.localize(parsed_date)
print(mexico_city_datetime)