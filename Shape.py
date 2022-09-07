from re import X
import pygame
from abc import ABC, abstractmethod

class Shape():
    def __init__(self,widht,height,x_coordinate,y_coordinate,color,surface):
        self.widht = widht
        self.height = height
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.color = color
        self.surface = surface
    
    @abstractmethod
    def draw(self):
        pass

class Square(Shape):
    def draw(self):
        pygame.draw.rect(self.surface, self.color, pygame.Rect(self.x_coordinate, self.y_coordinate, self.widht, self.height))
        pygame.display.flip()