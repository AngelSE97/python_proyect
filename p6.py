'''
import os

ruta = 'C:\\Users\\luis.santibanez\\python_proyect\\ey\\otrs\\Prueba2.txt'

a=os.path.split(ruta)
print(a)'''
from pathlib import Path,PureWindowsPath

carpeta = Path ('C:/Users/luis.santibanez/python_proyect/Prueba.txt')

ruta= PureWindowsPath(carpeta)

print(ruta)