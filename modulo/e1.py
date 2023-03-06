from collections import Counter, defaultdict,namedtuple
import os
import shutil
import send2trash

numeros = [1,8,4,1,5,2,5,6,8,8,6,4,8,5]
frase = 'la puerca esta en la posilga'
#print(Counter(numeros))
#print(Counter(frase.split()))


serie = Counter([1,5,8,5,9,8,4,8,5,4,8,4,5,4,8,7,4,5,4,1,2,5,2,5,5])

#print(serie.most_common(1))

#print(list(serie))

#mi_dic={'uno':'verde','dos':'rojo','tres':'azul'}

#mi_dic = defaultdict(lambda: 'nada')

#mi_dic['uno'] = 'verde'

#print(mi_dic['dos'])
#print(mi_dic)

#persona = namedtuple('persona',['nombre','altura','peso'])
#ariel = persona('Ariel',1.76,60)

#print(ariel)
'''
print(os.getcwd())

archivo = open('curso.txt','w')

archivo.write('texto de prueba')
archivo.close()

print(os.listdir())

shutil.move('curso.txt','C:\\Users\\luis.santibanez\\Desktop')'''

#send2trash.send2trash('curso.txt')

ruta='C:\\Users\\luis.santibanez\\Desktop'
for carpeta,subcarpeta, archivo in os.walk(ruta):
    print(f'en la carpeta: {ruta}')
    print(f'las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('LOS ARCHIVIS SIN:')
    for arch in archivo:
        if arch.startswith('virtual'):
            print(f'\t{sub}')
    print('\n')
