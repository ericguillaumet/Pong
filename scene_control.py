from screens import *
from utilites import HEIGHT, WIDTH

class SceneControl:
    def __init__(self):
        self.main_screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Pong")
        self.refresh_rate = pg.time.Clock()
        """
        self.game = Game(self.main_screen, self. refresh_rate)
        self.menu = Menu(self.main_screen, self. refresh_rate)
        self.results = Result(self.main_screen, self. refresh_rate)
        self.records = Records(self.main_screen, self. refresh_rate)
        """
        self.screens = [Menu(self.main_screen, self. refresh_rate), Game(self.main_screen, self. refresh_rate), Result(self.main_screen, self. refresh_rate)]

        self.result_value = ""

    def start(self):
        keep_going = True

        index = 0

        while keep_going:
            
            if index == 1:
                close = self.result_value = self.screens[index].screen_loop()
                if close == True:
                    break
                index += 1

            elif index == 2:
                self.screens[index].get_result(self.result_value)
                close = self.screens[index].screen_loop()
                if close == True:
                    break

                index = 0

            elif index == 0:
                close = self.screens[index].screen_loop()
                if close == 'records':
                    self.screens[3].screen_loop()
                if close == True:    
                    break
                index += 1

                if close == True:
                    break
        
 

        """
        close = self.menu.screen_loop()
        if close == True:
            break

        close = self.result_value = self.game.frame_loop()
        if close == True:
            break

        self.results.get_result(self.result_value)
        
        close = self.results.screen_loop()
        if close == True:
            break
        
        """