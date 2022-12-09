import pygame as pg
from class_figure import Ball, Racket

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 94)
ORANGE = (255, 172, 28)
RED = (255, 0, 0)
FPS = 280
FIRST_NOTICE = 10000
SECOND_NOTICE = 5000

class Game:
    def __init__(self):
        pg.init()
        self.main_screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Pong")
        self.refresh_rate = pg.time.Clock()
        self.ball = Ball(WIDTH//2, HEIGHT//2, vx = 2, vy = 2)
        self.racket1 = Racket(10, HEIGHT//2, vy = 5)
        self.racket2 = Racket(WIDTH - 10, HEIGHT//2, vy = 5)
        self.font = pg.font.Font("fonts/ZenDots.ttf", 15)
        self.timerFont = pg.font.Font("fonts/ZenDots.ttf", 20)
        self.scoreboard1 = 0
        self.scoreboard2 = 0
        self.whogoals = ""
        self.timer = 15000 #En milisegundos
        self.background_color = GREEN
        self.frame_count = 0

    def frame_loop(self):
        
        game_over = False

        while not game_over and (self.scoreboard1 < 10 or self.scoreboard2 < 10) and self.timer > 0: #Mientras el marcador sea menor a 10 el juego sigue. Además el temporizador debe ser mayor a cero
            
            time_jump = self.refresh_rate.tick(FPS) #variable para controlar la velocidad entre fotogramas // 1000/280 = cantidad de fotogramas por segundo
            self.timer -= time_jump 

            if self.timer == 0: #Si el temporizador llega a 0, Game Over.
                game_over = True
        
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_over = True
            
            self.racket1.move(pg.K_w, pg.K_s) #Mover raqueta izquierda
            self.racket2.move(pg.K_UP, pg.K_DOWN) #Mover raqueta derecha
            self.whogoals = self.ball.move() #Mover pelota
            
            self.main_screen.fill(self.background())

            if self.whogoals == "right":
                self.scoreboard1 += 1
            elif self.whogoals == "left":
                self.scoreboard2 += 1
            
            #self.main_screen.fill(GREEN) #Pintar la pantalla // Desactivo para que no pinte después del if self.timer 
            self.ball.crash_check(self.racket1,self.racket2) #Lógica de choque

            self.scoreboard()
            self.dashed_line()

            time = self.font.render(str(int(self.timer/1000)), 0, WHITE) #Le añadimos int para que muestre solamente los segundos como unidades, str para que lo convierta a string
            self.main_screen.blit(time, (410, 20))
            #self.ball.scoreboard(self.main_screen) #Establecer el marcador, hay que ponerlo después de pantalla, para que no se sobrepongan.

            self.ball.draw(self.main_screen) #Pintar la pelota
            self.racket1.draw(self.main_screen) #Pintar la raqueta 1
            self.racket2.draw(self.main_screen) #Pintar la raqueta 2

            self.player_name()

            pg.display.flip() #Para activar los colores
    
        pg.quit()

    def player_name(self):
        player1 = self.font.render("Player 1", 0, YELLOW)
        player2 = self.font.render("Player 2", 0, YELLOW)
        self.main_screen.blit(player1, (160, 30))
        self.main_screen.blit(player2, (560, 30))

    def scoreboard(self):
        SCLeft = self.font.render(str(self.scoreboard2), 0, (YELLOW))
        SCRight = self.font.render(str(self.scoreboard1), 0, (YELLOW))
        self.main_screen.blit(SCRight, (200, 50))
        self.main_screen.blit(SCLeft, (600, 50))

    def background(self): #fijar fondo de pantalla
        
        self.frame_count += 1
        
        if self.timer > FIRST_NOTICE: #Aún no entra ninguna condición
            self.frame_count = 0

        elif self.timer > SECOND_NOTICE: #Si es menor a 10000 milisegundos, pintar pantalla en naranja parpadenado

            if self.frame_count == 20: #Velocidad de parpadeo
                if self.background_color == GREEN:
                    self.background_color = ORANGE 
                else:
                    self.background_color = GREEN
                self.frame_count = 0

        else: #Si no cumple ninguna de las otras dos condiciones, 5 segundos, entra en el parpadeo en rojo
            if self.frame_count == 20:
                if self.background_color == ORANGE:
                    self.background_color = RED 
                else:
                    self.background_color = ORANGE
                self.frame_count = 0

        return self.background_color

    def dashed_line(self):
        line_count1 = 0
        line_count2 = 50

        while line_count1 <= 560 and line_count2 <= 630: #Para crear líneas intermitentes

            pg.draw.line(self.main_screen, WHITE, (400, line_count1), (400, line_count2), width = 10) #Pintar linía blanca
            line_count1 += 70
            line_count2 += 70