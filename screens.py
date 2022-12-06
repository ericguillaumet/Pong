import pygame as pg
from class_figure import Ball, Racket

WIDTH = 800
HEIGHT = 600

class Game:
    def __init__(self):
        pg.init()
        self.main_screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Pong")
        self.refresh_rate = pg.time.Clock()

        self.ball = Ball(WIDTH//2, HEIGHT//2, vx = 2, vy = 2)
        self.racket1 = Racket(10, HEIGHT//2, vy = 5)
        self.racket2 = Racket(WIDTH-10, HEIGHT//2, vy = 5)

        self.font = pg.font.Font(None, 30)

    def frame_loop(self):
        
        game_over = False

        while not game_over:
            #imprimir los milisegundos que tarda cada fot ograma actualmente
            self.refresh_rate.tick(280) #variable para controlar la velocidad entre fotogramas
                
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_over = True
            
            self.racket1.move(pg.K_w, pg.K_s) #Mover raqueta izquierda
            self.racket2.move(pg.K_UP, pg.K_DOWN) #Mover raqueta derecha
            self.ball.move() #Mover pelota

            self.main_screen.fill((0, 128, 94)) #Pintar la pantalla
            self.ball.scoreboard(self.main_screen) #Establecer el marcador, hay que ponerlo después de pantalla, para que no se sobrepongan.
            
            #lógica de choque
            #ball.crash_check(racket1, racket2)
            self.ball.crash_check(self.racket1,self.racket2)
            line_count1 = 0
            line_count2 = 50

            while line_count1 <= 560 and line_count2 <= 630: #Para crear líneas intermitentes

                pg.draw.line(self.main_screen, (255, 255, 255), (400, line_count1), (400, line_count2), width = 10) #Pintar linía blanca
                line_count1 += 70
                line_count2 += 70

            self.ball.draw(self.main_screen) #Pintar la pelota
            self.racket1.draw(self.main_screen) #Pintar la raqueta 1
            self.racket2.draw(self.main_screen) #Pintar la raqueta 2

            self.player_name()

            pg.display.flip() #Para activar los colores
    
        pg.quit()

    def player_name(self):
        player1 = self.font.render("Player 1", 0, (255, 255, 0))
        player2 = self.font.render("Player 2", 0, (255, 255, 0))
        self.main_screen.blit(player1, (200, 50))
        self.main_screen.blit(player2, (600, 50))