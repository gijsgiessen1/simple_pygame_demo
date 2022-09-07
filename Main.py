import pygame.event
import Window
from Shape import Square
class Main():
    def __init__(self):
        self.running = True
    
    def run(self):
        while self.running:
            game_window = Window.Window(300,400)
            square = Square(40,40,150,200,(34,139,34),game_window.get_window())
            square.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Usually wise to be able to close your program.
                    raise SystemExit
                
            