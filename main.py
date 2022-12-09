from screens import Game, Menu #importamos las clases

game = Game() #Creamos el objeto de la clase Partida

menu = Menu()
mensaje = menu.screen_loop()

if mensaje == "Play":
    game.frame_loop()