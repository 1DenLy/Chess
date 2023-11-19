import pygame

# Инициализация Pygame
pygame.init()

#Constants
FIGURESIZE = 80

class mainFigure:
    def __init__ (self, x_position: int, y_position: int, imageObjectPath, cellPositionX: str, cellPositionY: str, sizeObject: int = FIGURESIZE): 

        self.rect = pygame.Rect(x_position, y_position, sizeObject, sizeObject)
        imageObjectPath = pygame.image.load(imageObjectPath).convert_alpha()
        self.imageObject = pygame.transform.scale(imageObjectPath, (sizeObject, sizeObject))
        self.x_position = x_position
        self.y_position = y_position

        self.cellPositionX = cellPositionX
        self.cellPositionY = cellPositionY

    def draw(self, surface):
        surface.blit(self.imageObject, self.rect.center)


    def createFigure(x_position, y_position, imageObject, cell_x, cell_y):
        figure = mainFigure(x_position, y_position, imageObject, cell_x, cell_y)
        return figure