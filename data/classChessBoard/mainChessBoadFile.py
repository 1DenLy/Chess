import pygame
import sys

# Инициализация Pygame
pygame.init()



# Константы
WIDTH, HEIGHT = 750, 825  # Увеличил ширину окна для добавления пустого места по бокам
FPS = 60
WHITE = (240, 240, 240)
BLACK = (0, 0, 0)




# Класс клетки
class ChessBoard:
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def creatingCellsDesc() -> list: # Создание списка клеток шахматной доски
        
        cells = []
        cell_size = 80

        for row in range(9):
            for col in range(8):

                x = col * cell_size + 50    # Добавил смещение по X
                y = row * cell_size + 50    # Добавил смещение по Y
                
                if (row + col) % 2 == 0:
                    color = WHITE
                else:
                    color = BLACK
                
                cell = ChessBoard(x, y, cell_size, color)
                cells.append(cell)
        
        return cells
