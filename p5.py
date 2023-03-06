'''mi_archivo = open('Prueba.txt','a')


lista = ['roard','acdc','rock']

for i in lista:
    mi_archivo.writelines(i + '\n')

mi_archivo.close()'''

registro_ultima_sesion = ["Federico\t", "20/12/2021\t", "08:17:32 hs\t", "Sin errores de carga\t"]

archivoA = open("registro.txt", "a")
archivoA.writelines(registro_ultima_sesion)
archivoA.close()

archivoR = open("registro.txt", "r")
for linea in archivoR:
    print(linea.rstrip())