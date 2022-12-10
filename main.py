from screens import Game, Menu, Result#importamos las clases

game = Game()
value_result = game.frame_loop()
print("El resultado", value_result)
result = Result(value_result) #Para utilizar una clase siempre debemos crear un objeto, en este caso la variable result
result.screen_loop()

"""
game = Game() #Creamos el objeto de la clase Partida

menu = Menu()
mensaje = menu.screen_loop()

if mensaje == "Play":
    game.frame_loop()

"""