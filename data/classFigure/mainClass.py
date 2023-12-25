import pygame
from data.classChessBoard.mainChessBoadFile import Cells

# Инициализация Pygame
pygame.init()

#Constants
FIGURESIZE = 80

BLACKLIST, WHITELIST, FULL_LIST = [], [], []


class mainFigure:
    def __init__ (self, x_position: str, y_position: str, imageObjectPath,  sizeObject: int = FIGURESIZE, figureOnBoard: bool = True, figureSelected: bool = False, figure_type: str = 'None'): 

        self.x_position = Cells[(x_position+y_position)][0] + 40
        self.y_position = Cells[(x_position+y_position)][1] + 40

        self.rect = pygame.Rect(self.x_position, self.y_position, sizeObject, sizeObject)
        self.imageObjectPath = imageObjectPath
        imageObject = pygame.image.load(imageObjectPath).convert_alpha()
        self.imageObject = pygame.transform.scale(imageObject, (sizeObject, sizeObject))
        
        self.cellPositionLitter = x_position
        self.cellPositionNum = y_position
        self.figureOnBoard = figureOnBoard
        self.figureSelected = figureSelected
        self.figure_type = figure_type


    def draw(self, surface: pygame.Surface):

        if self.figureOnBoard: 

            surface.blit(self.imageObject, self.rect)
        

    def updatePosition(self, new_x_Position, new_y_Position):
        self.x_position = new_x_Position
        self.y_position = new_y_Position
        self.rect = pygame.Rect(self.x_position, self.y_position, FIGURESIZE, FIGURESIZE)


    def createFigure(x_position, y_position, imageObject):

        figure = mainFigure(x_position, y_position, imageObject)
        figure.__addToListWhenCreated()

        return figure


    def __addToListWhenCreated(object: 'mainFigure') -> list:
        
        FULL_LIST.append(object)

        if object.imageObjectPath[-6] == 'w': WHITELIST.append(object)
            
        elif object.imageObjectPath[-6] == 'b': BLACKLIST.append(object)


    def selectedCells(listOfCells: list):

        mousePosition = pygame.mouse.get_pos()

        for cell in listOfCells:
            if cell.rect.collidepoint(mousePosition):
                pass


    def moveFigure():
        
        selectedFigure = mainFigure.changeFigure()
        print(selectedFigure.__class__)

        try:
            if selectedFigure.figureSelected:

                selectedFigure.updatePosition(x,y)
                selectedFigure.figureSelected = False

        except Exception:
            pass


    def changeFigure(selectedPlayer: str = 'White'):

        if selectedPlayer == 'White':
            desiredList = WHITELIST
        else: 
            desiredList = BLACKLIST

    
        mousePosition = pygame.mouse.get_pos()

        for figure in desiredList:
            
            if figure.figureSelected == False:
                if figure.rect.collidepoint(mousePosition):
                    figure.figureSelected = True
                    return figure


