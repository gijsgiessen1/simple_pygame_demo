import pygame

class Window():
    def __init__(self,width,height):
        self.screen = pygame.display.set_mode((width,height))
        # pygame.display.flip()

    def get_window(self):
        return self.screen

    
