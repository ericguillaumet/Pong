import pygame as pg
from utilites import WHITE, YELLOW

class Ball:

    def __init__(self, pos_x, pos_y, radius = 20, color = WHITE, vx = 1, vy = 1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.color = color
        self.vx = vx
        self.vy = vy
        self.counter_left = 0
        self.counter_right = 0
        self.font = pg.font.Font(None, 40) #Esto esta fuera del while

    def draw(self, screen):
        pg.draw.circle(screen, self.color,(self.pos_x, self.pos_y), self.radius)

    def move(self, y_max = 600, x_max = 800):
        self.pos_x += self.vx
        self.pos_y += self.vy

        if self.pos_y >= y_max - self.radius or self.pos_y < 0 + self.radius: # + self para que no se unda la pelota // para que rebote arriba y
            self.vy *= -1

        #El objetivo es que la pelota desaparezca en los límites y vuelva a aparecer desde el centro

        if self.pos_x >= x_max + self.radius * 10: #límite derecho
            self.counter_right += 1
            #Para que la pelota salga desde el centro
            self.pos_x = x_max // 2
            self.pos_y = y_max // 2

            self.vx *= -1
            self.vy *= -1

            return "right"
            
        if self.pos_x < 0 - self.radius * 10: #límite izquierdo
            self.counter_left += 1
            #Para que la pelota salga desde el centro
            self.pos_x = x_max // 2
            self.pos_y = y_max // 2

            self.vx *= -1
            self.vy *= -1

            return "left"

    def scoreboard(self, main_screen):
        SCLeft = self.font.render(str(self.counter_right), 0, (YELLOW))
        SCRight = self.font.render(str(self.counter_left), 0, (YELLOW))
        main_screen.blit(SCRight, (200, 50))
        main_screen.blit(SCLeft, (600, 50))
     
    @property #Para transformar los métodos cómo variables
    def right(self):
        return self.pos_x + self.radius
    @property
    def left(self):
        return self.pos_x - self.radius
    @property
    def up(self):
        return self.pos_y - self.radius
    @property
    def down(self):
        return self.pos_y + self.radius

    def crash_check(self, *rackets):
        for r in rackets:
            if self.right >= r.left and\
                self.left <= r.right and\
                self.down >= r.up and\
                self.up <= r.down:
                    self.vx *= -1
                    break

class Racket: 
    
    def __init__(self, pos_x, pos_y, w = 20, h = 100, color = WHITE, vx = 1, vy = 1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.color = color
        self.vx = vx
        self.vy = vy

    def draw(self, screen):
        pg.draw.rect(screen, self.color,(self.pos_x - (self.w // 2),self.pos_y - (self.h // 2), self.w, self.h))

    def move(self, key_up, key_down, y_max = 600, y_min = 0):
        key_status = pg.key.get_pressed()
        
        if key_status[key_up] == True and self.pos_y > (y_min + self.h // 2): #Para que cuando llegue a 550 pare, para que no se pierda media raqueta
            self.pos_y -= 5 #Velocidad de la raqueta en eje Y

        if key_status[key_down] == True and self.pos_y < (y_max - self.h // 2):
            self.pos_y += 5

    #Para poder llamar la función como una variable

    @property
    def right(self):
        return self.pos_x + self.w//2

    @property
    def left(self):
        return self.pos_x - self.w//2

    @property
    def up(self):
        return self.pos_y - self.h//2

    @property
    def down(self):
        return self.pos_y + self.h//2