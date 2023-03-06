"""lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for i, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(nombre)
lista_indices = list(enumerate("Python"))
print(lista_indices)"""
"""
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

pa = list(zip(capitales,paises))

for capitales,paises in pa:
    print(f"La capital de {paises} es {capitales}")"""

def check(lista):

    lts = []

    for n in lista:
        if n in range (1,1000):
            lts.append(n)
        else:
            pass
    return lts

resultado = check([99,97,1001])
print(resultado)