from screens import *

class SceneControl:
    def __init__(self):
        self.game = Game()
        self.menu = Menu()
        self.results = Result()
        self.records = Records()

        self.result_value = ""

    def start(self):
        self.menu.screen_loop()
        self.result_value = self.game.frame_loop()
        self.results.get_result(self.result_value)
        self.results.screen_loop()