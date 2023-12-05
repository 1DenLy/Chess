import pygame
from data.classFigure.mainClass import mainFigure

# Инициализация Pygame
pygame.init()


class pawnFigure(mainFigure):
    def __init__(self):
        super().__init__()