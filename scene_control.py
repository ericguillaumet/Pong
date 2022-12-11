from screens import *

class SceneControl:
    def __init__(self):
        self.game = Game()
        self.menu = Menu()
        self.results = Result()
        self.records = Records()

        self.result_value = ""
        #como tarea: mejorar el while dentro del método start

    def start(self):
        keep_going = True

        while keep_going:
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