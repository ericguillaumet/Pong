import pygame as pg
from class_figure import Ball, Racket

pg.init() #Método para iniciar pygame

main_screen = pg.display.set_mode((800, 600)) #Establecer la pantalla
pg.display.set_caption("Pong") #Establecer nombre del juego

#Definir la tasa de refresco de nuestro bucle de fotrogramas FPS (Fotograma Por Segundo)

chronometer = pg.time.Clock()

#Ojbetos pelota y raqueta
ball = Ball(400, 300)
racket1 = Racket(10, 300)
racket2 = Racket(790, 300) 

#Asignando velocidad
racket1.vy = 6
racket2.vy = 6
ball.vx = 3

game_over = False

initial = 0
final = 0

while not game_over:
    
    #imprimir los milisegundos que tarda cada fot ograma actualmente
    tv = chronometer.tick(280) #tv: time value // variable para controlar la velocidad entre fotogramas
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
    
    racket1.move(pg.K_w, pg.K_s) #Mover raqueta izquierda
    racket2.move(pg.K_UP, pg.K_DOWN) #Mover raqueta derecha
    ball.move() #Mover pelota

    main_screen.fill((0, 128, 94)) #Pintar la pantalla
    #ball.scoreboard(main_screen) #Establecer el marcador, hay que ponerlo después de pantalla, para que no se sobrepongan.
    
    #lógica de choque
    #ball.crash_check(racket1, racket2)
    ball.crash_checkV2(racket1, racket2)

    pg.draw.line(main_screen, (255, 255, 255), (400, 0), (400, 600), width = 2) #Pintar linía blanca
    
    ball.draw(main_screen) #Pintar la pelota
    racket1.draw(main_screen) #Pintar la raqueta 1
    racket2.draw(main_screen) #Pintar la raqueta 2

    pg.display.flip() #Para activar los colores