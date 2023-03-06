import pygame
import random
import math
from pygame import mixer
import io

#fuente
def fuente_bytes(fuente):
    #abre archivo en forma binaria
    with open (fuente,'rb') as f:
        #almacena los bytes del archivo en una variable
        ttr_bytes = f.read()
         #crea un objeto bytesio a partir de los bites del archivo
    return io.BytesIO(ttr_bytes)

#inicializar game
pygame.init()
#crea la pantalla
pantalla = pygame.display.set_mode((800,600))

#titulo e icono
pygame.display.set_caption('INVACION')
icono = pygame.image.load('alien (1).png')
pygame.display.set_icon(icono)

#fondo
fondo= pygame.image.load('Fondo.jpg')

#musica de fondo
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.2)#volumen del 0 - 1
mixer.music.play(-1)#se repite al acabar

#jugador
juga = pygame.image.load('ovni (1).png')
juga_x = 368
juga_y = 536
juga_x_cambio = 0
juga_y_cambio = 0

#enemigo
neme = []
neme_x = []
neme_y = []
neme_x_cambio = []
neme_y_cambio = []
cantidad_enemigos= 8

for e in range(cantidad_enemigos):
    neme.append(pygame.image.load('crowd.png'))
    neme_x.append(random.randint(0, 736))
    neme_y.append(random.randint(50, 200))
    neme_x_cambio.append(0.3)
    neme_y_cambio.append(50)
'''    
neme = pygame.image.load('crowd.png')
neme_x = random.randint(0,736)
neme_y = random.randint(50,200)
neme_x_cambio = 0.3
neme_y_cambio = 50
'''

#bala
bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 2
bala_visible = False

#SCORE
puntaje=0
fuente_como_bytes = fuente_bytes('FreeSansBold.ttf')
fuente = pygame.font.Font(fuente_como_bytes,32)
texto_x = 10
texto_y = 10

#texto final
finality = pygame.font.Font(fuente_como_bytes,32)


#funcion mostrar pumtaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f'Puntaje {puntaje}',True,(255,255,255))
    pantalla.blit(texto,(x,y))

#funcion jugador
def jugador(x,y):
    pantalla.blit(juga,(x,y))

#funcion enemigo
def nemesis(x,y,ene):
    pantalla.blit(neme[ene],(x,y))

#funcion bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(bala,(x+16,y+10))

#funcion detectar colisiones
def hay_colision(x_1,y_1,x_2,y_2):
    distancia=math.sqrt(math.pow(x_1-x_2,2)+math.pow(y_2-y_1,2))
    if distancia < 27:
        return True
    else:
        return False

#game over

def game_over():
    fuente_final = finality.render('INVASION TERMINADA', True,(255,255,255))
    pantalla.blit(fuente_final,(200,200))



#loop de juegp
se_ejecuta= True
while se_ejecuta:

    # color de pantalla
    #pantalla.fill((205, 205, 228))
    #imagen de fondo
    pantalla.blit(fondo,(0,0))

    #iterar eventos
    for evento in pygame.event.get():

        #evento cerrar juego
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #movimiento del jugador
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                juga_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                juga_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                balazo = mixer.Sound('disparo.mp3')
                balazo.play()
                if not bala_visible:
                    bala_x = juga_x
                    disparar_bala(bala_x,bala_y)



        #evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                juga_x_cambio = 0

    #modifica la posicion del jugador
    juga_x += juga_x_cambio
    #mantener dentro de bordes al jugador
    if juga_x <= 0:
        juga_x = 736
    elif juga_x >= 736:
        juga_x = 0

    # modifica la posicion del enemigo
    for e in range(cantidad_enemigos):
        #fin del juego
        if neme_y[e] > 500:#altura para terminar el juego
            for l in range(cantidad_enemigos):
                neme_y[e] = 1000
            game_over()
            break

        neme_x[e] += neme_x_cambio[e]
        # mantener dentro de bordes al enemigo
        if neme_x[e] <= 0:
            neme_x_cambio[e] = 0.3
            neme_y[e] += neme_y_cambio[e]
        elif neme_x[e] >= 736:
            neme_x_cambio[e] = -0.3
            neme_y[e] += neme_y_cambio[e]

            # colision
        colision = hay_colision(neme_x[e], neme_y[e], bala_x, bala_y)
        if colision:
            destruccion = mixer.Sound('Golpe.mp3')
            destruccion.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            print((puntaje))
            neme_x[e] = random.randint(0, 736)
            neme_y[e] = random.randint(50, 200)

        nemesis(neme_x[e], neme_y[e],e)

    '''
    if neme_x <= 0:
        neme_x_cambio = 0.3
        neme_y += neme_y_cambio
    elif neme_x >= 736:
        neme_x_cambio = -0.3
        neme_y += neme_y_cambio'''

    #movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio




    jugador(juga_x,juga_y)
    #mostrar puntaje
    mostrar_puntaje(texto_x,texto_y)
    #actualiza la pantalla
    pygame.display.update()

