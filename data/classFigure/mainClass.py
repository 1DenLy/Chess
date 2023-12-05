import pygame

from data.classChessBoard.mainChessBoadFile import Cells

# Инициализация Pygame
pygame.init()

#Constants
FIGURESIZE = 80

BLACKLIST, WHITELIST = [], []


class mainFigure:
    def __init__ (self, x_position: str, y_position: str, imageObjectPath,  sizeObject: int = FIGURESIZE, figureOnBoard: bool = True): 

        self.x_position = Cells[(x_position+y_position)][0]
        self.y_position = Cells[(x_position+y_position)][1]
        self.rect = pygame.Rect(self.x_position, self.y_position, sizeObject, sizeObject)
        self.imageObjectPath = imageObjectPath
        imageObject = pygame.image.load(imageObjectPath).convert_alpha()
        self.imageObject = pygame.transform.scale(imageObject, (sizeObject, sizeObject))
        
        self.cellPositionLitter = x_position
        self.cellPositionNum = y_position
        self.figureOnBoard = figureOnBoard

    def draw(self, surface: pygame.Surface):
        if self.figureOnBoard:
            surface.blit(self.imageObject, self.rect.center)


    def __addToListWhenCreated(object: 'mainFigure') -> list:
        if object.imageObjectPath[-6] == 'w':
            WHITELIST.append(object)
        elif object.imageObjectPath[-6] == 'b':
            BLACKLIST.append(object)



    def createFigure(x_position, y_position, imageObject):
        figure = mainFigure(x_position, y_position, imageObject)
        return figure