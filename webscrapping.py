import bs4
import requests

'''
resultado = requests.get('https://coronavirus.gob.mx/')
#print(resultado.text)
#transforma el codigo a una cadena string
sopa = bs4.BeautifulSoup(resultado.text,'lxml')
#traemos los parrafos de una clase
sana = sopa.select('.elementor-row p')
for p in sana:

    print(p.getText())'''
#sacar imagenes de webs (para las clases con nombres con espacios se les remplaza por un punto)
'''
sopa = bs4.BeautifulSoup(resultado.text,'lxml')

imagenes = sopa.select('.attachment-medium')[0]['data-src']

#print(imagenes)

imagen_pb =  requests.get(imagenes)

f = open('imag.jpg','wb')
f.write(imagen_pb.content)
f.close()'''

url_base = 'http://books.toscrape.com/catalogue/page-{}.html'
#loop para traer 15 pag de una web
'''
for n in range (1,15):
    print(url_base.format(n))
'''
#obtener nombres de libros
'''
resultados = requests.get(url_base.format('1'))

sopa = bs4.BeautifulSoup(resultados.text,'lxml')

libros = sopa.select('.product_pod')
ejemplo = libros[0].select('a')[1]['title']
print(ejemplo)'''

titulos_rating = []
for n in range (1,15):
    #crear sopa pára cada pag
    url_pag = url_base.format(n)
    resultado = requests.get(url_pag)
    sopa = bs4.BeautifulSoup(resultado.text,'lxml')

    #seleccionar datos libro
    libros = sopa.select('.product_pod')
    #iterar cada libro
    for libro in libros:

        if len(libro.select('.star-rating.Four')) or len(libro.select('.star-rating.Five')):

            #guardar libro
            titulo_lib = libro.select('a')[1]['title']
            #agregar a la lista
            titulos_rating.append(titulo_lib)
for t in titulos_rating:

    print(t)