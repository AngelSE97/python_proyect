import pytz
from datetime import datetime
from dateutil import parser

fecha_str = "2022-01-01T12:00:00EST"
tzinfos = {"EST": pytz.timezone("America/Mexico_City")}
fecha = parser.parse(fecha_str, tzinfos=tzinfos)
print(fecha)
print(tzinfos)