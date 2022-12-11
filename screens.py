import pygame as pg
from class_figure import Ball, Racket
from utilites import *

class Game:

    def __init__(self):
        self.main_screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Pong")
        self.refresh_rate = pg.time.Clock()
        self.ball = Ball(WIDTH//2, HEIGHT//2, vx = 2, vy = 2)
        self.racket1 = Racket(10, HEIGHT//2, vy = 5)
        self.racket2 = Racket(WIDTH - 10, HEIGHT//2, vy = 5)
        self.font = pg.font.Font("fonts/ZenDots.ttf", 15) #Elijo el directorio donde está la imágen
        self.timerFont = pg.font.Font("fonts/ZenDots.ttf", 20)
        self.scoreboard1 = 0
        self.scoreboard2 = 0
        self.whogoals = ""
        self.timer = TIME_LIMIT #En milisegundos
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

        return self.final_result()

        

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

    def final_result(self):
        if self.scoreboard1 > self.scoreboard2:
            return f"Player two wins. Result: Player 1: {self.scoreboard2} Player 2: {self.scoreboard1}"
        elif self.scoreboard2 > self.scoreboard1:
            return f"Player one wins. Result: Player 1: {self.scoreboard2} Player 2: {self.scoreboard1}"
        else:
            return f"You ended in a tie. Result: Player 1: {self.scoreboard2} Player 2: {self.scoreboard1}"

class Menu:
    def __init__(self):
        self.main_screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Menu")
        self.refresh_rate = pg.time.Clock()

        self.background_image = pg.image.load("images/portada.jpg") #Elijo el directorio donde está la imágen
        self.font_menu = pg.font.Font("fonts/ZenDots.ttf", 20)

    def screen_loop(self):
        game_over = False

        while not game_over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_over = True

                if event.type == pg.KEYDOWN: #KEYDOWN para llamar a cualquier tecla del teclado
                    if event.key == pg.K_RETURN: #key llama los distintos eventos de teclado
                        game_over = True

                    elif event.key == pg.K_r: #key llama los distintos eventos de teclado
                        game_over = True
                    

            self.main_screen.blit(self.background_image, (0, 0))
            play = self.font_menu.render("Press RETURN to start", 0, WHITE)
            record = self.font_menu.render("Press R to check records", 0, WHITE)
            self.main_screen.blit(play, (WIDTH // 2, 450))
            self.main_screen.blit(record, (WIDTH // 2, 400))
            pg.display.flip()

class Result:

    def __init__(self):
        self.main_screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Result")
        self.refresh_rate = pg.time.Clock()

        self.background_image = pg.image.load("images/portada.jpg") #Elijo el directorio donde está la imágen
        self.font_result = pg.font.Font("fonts/ZenDots.ttf", 15)
        self.result = ""

    def screen_loop(self):
        game_over = False

        while not game_over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_over = True

            if event.type == pg.KEYDOWN: #KEYDOWN para llamar a cualquier tecla del teclado
                if event.key == pg.K_RETURN: #key llama los distintos eventos de teclado
                    game_over = True
                    return "Play"

            #self.main_screen.blit(self.background_image, (0, 0))
            self.main_screen.fill(WHITE)
            result = self.font_result.render(self.result, 0, YELLOW)
            self.main_screen.blit(result, (145, 450))
            pg.display.flip() 

    def get_result(self, result):
        self.result = result

class Records:

    def __init__(self, result):
            self.main_screen = pg.display.set_mode((WIDTH, HEIGHT))
            pg.display.set_caption("Records")
            self.refresh_rate = pg.time.Clock()

            self.background_image = pg.image.load("images/portada.jpg") #Elijo el directorio donde está la imágen
            self.font_result = pg.font.Font("fonts/ZenDots.ttf", 15)
            self.result = result

    def screen_loop(self):
        game_over = False

        while not game_over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_over = True

            if event.type == pg.KEYDOWN: #KEYDOWN para llamar a cualquier tecla del teclado
                if event.key == pg.K_RETURN: #key llama los distintos eventos de teclado
                    game_over = True
                    
            self.main_screen.fill(WHITE)
            result = self.font_result.render("RECORDS", 0, YELLOW)
            self.main_screen.blit(result, (145, 450))
            pg.display.flip() 