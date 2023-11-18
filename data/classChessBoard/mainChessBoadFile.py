import pygame

# Инициализация Pygame
pygame.init()



# Константы
WIDTH, HEIGHT = 750, 825  # Увеличил ширину окна для добавления пустого места по бокам
FPS = 60
WHITE = (240, 240, 240)
BLACK = (0, 0, 0)

LISTOFNUMBER = ("1", "2", "3", "4", "5", "6", " 7", "8", "9")
LISTOFLETTERS = ("A", "B", "C", "D", "E", "F ", "G", "H")
FONT = pygame.font.Font(None, 36)

# Класс клетки
class ChessBoard:
    def __init__(self, x_position: int, y_position: int, sizeObject: int, colorObject, cellPositionX: str = -20, cellPositionY: str = -20):
        self.rect = pygame.Rect(x_position, y_position, sizeObject, sizeObject)
        self.color = colorObject
        self.cellPositionX = cellPositionX
        self.cellPositionY = cellPositionY

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    
    def drawCellsNumerated(surface, listOfCells): # draw cells with numbers and letters 
        for cell in listOfCells:
            if cell.cellPositionY in LISTOFNUMBER and cell.cellPositionX == "A":
                text = FONT.render(cell.cellPositionY, True, BLACK)
                text_rect = text.get_rect(center=(cell.rect.x - 30, cell.rect.centery))  # Расположение текста по X
                surface.blit(text, text_rect)

            if cell.cellPositionX in LISTOFLETTERS and cell.cellPositionY == "1":
                text = FONT.render(cell.cellPositionX, True, BLACK)
                text_rect = text.get_rect(center=(cell.rect.centerx, cell.rect.y - 30))  # Расположение текста по Y
                surface.blit(text, text_rect)

    def creatingCellsDesc() -> list: # Create a list of cells 
        
        listOfCells = []
        cellSize = 80

        for row in range(9):

            cellPositionY = LISTOFNUMBER[row]

            for column in range(8):


                cellPositionX = LISTOFLETTERS[column]

                x_position = column * cellSize + 50    # Добавил смещение по X
                y_position = row * cellSize + 50    # Добавил смещение по Y
                
                # Change color of the cells
                if (row + column) % 2 == 0:
                    colorObject = WHITE
                else:
                    colorObject = BLACK
                # Creating the cells for the list
                cell = ChessBoard(x_position, y_position, cellSize, colorObject, cellPositionX, cellPositionY)
                listOfCells.append(cell)
        
        return listOfCells
