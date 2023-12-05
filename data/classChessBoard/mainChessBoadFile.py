import pygame

# Инициализация Pygame
pygame.init()



# Константы
WIDTH, HEIGHT = 750, 825  # Увеличил ширину окна для добавления пустого места по бокам
FPS = 60
WHITE = (210, 210, 210)
BLACK = (0, 56, 34)

LISTOFNUMBER = ("1", "2", "3", "4", "5", "6", " 7", "8", "9")
LISTOFLETTERS = ("A", "B", "C", "D", "E", "F", "G", "H")

Cells = {
    'A1': (10, 10), 'B1': (90, 10), 'C1': (170, 10), 'D1': (250, 10), 'E1': (330, 10), 'F1': (410, 10), 'G1': (490, 10), 'H1': (570, 10),
    'A2': (10, 90), 'B2': (90, 90), 'C2': (170, 90), 'D2': (250, 90), 'E2': (330, 90), 'F2': (410, 90), 'G2': (490, 90), 'H2': (570, 90),
    'A3': (10, 170), 'B3': (90, 170), 'C3': (170, 170), 'D3': (250, 170), 'E3': (330, 170), 'F3': (410, 170), 'G3': (490, 170), 'H3': (570, 170),
    'A4': (10, 250), 'B4': (90, 250), 'C4': (170, 250), 'D4': (250, 250), 'E4': (330, 250), 'F4': (410, 250), 'G4': (490, 250), 'H4': (570, 250),
    'A5': (10, 330), 'B5': (90, 330), 'C5': (170, 330), 'D5': (250, 330), 'E5': (330, 330), 'F5': (410, 330), 'G5': (490, 330), 'H5': (570, 330),
    'A6': (10, 410), 'B6': (90, 410), 'C6': (170, 410), 'D6': (250, 410), 'E6': (330, 410), 'F6': (410, 410), 'G6': (490, 410), 'H6': (570, 410),
    'A7': (10, 490), 'B7': (90, 490), 'C7': (170, 490), 'D7': (250, 490), 'E7': (330, 490), 'F7': (410, 490), 'G7': (490, 490), 'H7': (570, 490),
    'A8': (10, 570), 'B8': (90, 570), 'C8': (170, 570), 'D8': (250, 570), 'E8': (330, 570), 'F8': (410, 570), 'G8': (490, 570), 'H8': (570, 570),
    'A9': (10, 650), 'B9': (90, 650), 'C9': (170, 650), 'D9': (250, 650), 'E9': (330, 650), 'F9': (410, 650), 'G9': (490, 650), 'H9': (570, 650)
}

FONT = pygame.font.Font(None, 36)

CELLSIZE = 80


# Класс клетки
class ChessBoard:
    def __init__(self, x_position: int, y_position: int, sizeObject: int, colorObject, cellPositionX: str = -20, cellPositionY: str = -20):
        self.rect = pygame.Rect(x_position, y_position, sizeObject, sizeObject)
        self.color = colorObject
        self.cellPositionX = cellPositionX
        self.cellPositionY = cellPositionY


    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, self.rect)

    
    def drawCellsNumerated(list: list, surface): # draw cells with numbers and letters 

        for cell in list:

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

        for row in range(9):

            cellPositionY = LISTOFNUMBER[row]

            for column in range(8):

                cellPositionX = LISTOFLETTERS[column]

                x_position = column * CELLSIZE + 50    # Добавил смещение по X
                y_position = row * CELLSIZE + 50    # Добавил смещение по Y
                
                # Change color of the cells
                if (row + column) % 2 == 0:
                    colorObject = WHITE
                else:
                    colorObject = BLACK
                # Creating the cells for the list
                cell = ChessBoard(x_position, y_position, CELLSIZE, colorObject, cellPositionX, cellPositionY)
                listOfCells.append(cell)
        
        return listOfCells
