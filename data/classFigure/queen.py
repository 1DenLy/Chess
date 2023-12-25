import pygame
from data.classFigure.mainClass import mainFigure, FIGURESIZE

# Инициализация Pygame
pygame.init()


class queenFigure(mainFigure):
    def __init__(self, x_position, y_position, imageObjectPath, sizeObject=FIGURESIZE, figureOnBoard=True, figureSelected=False, type = 'None'):
        super().__init__(x_position, y_position, imageObjectPath, sizeObject, figureOnBoard, figureSelected, type)


