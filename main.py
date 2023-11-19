import sys
from data.classChessBoard.mainChessBoadFile import *
from data.classFigure import *

from data.classChessBoard.mainChessBoadFile import ChessBoard
from data.classFigure.queen import queenFigure

# Инициализация окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Шахматная доска")


# Создание клеток шахматной доски
listOfCells = ChessBoard.creatingCellsDesc()

# Create figure queen for the board
queen = queenFigure.createFigure(90, 10, "data/classFigure/Image/png-transparent-chess-piece-queen-king-chess.png", "A", "1")


# Главный цикл программы
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)


    # Отрисовка клеток шахматной доски
    for cell in listOfCells:
        cell.draw(screen)
        

    # Отрисовка линий для разделения пространства счетчика времени
    pygame.draw.line(screen, BLACK, (50, 48), (50, 770), 2)  # Левая граница
    pygame.draw.line(screen, BLACK, (690, 48), (690, 770), 2)  # Правая граница
    pygame.draw.line(screen, BLACK, (50, 48), (690, 48), 2)  # Верх граница
    pygame.draw.line(screen, BLACK, (50, 770), (690, 770), 2)  # Нижняя граница

    ChessBoard.drawCellsNumerated(screen, listOfCells)

    


    # Draw the queen figure 
    queen.draw(screen)


    
    

    pygame.display.flip()
    clock.tick(FPS)

# Завершение программы
pygame.quit()
sys.exit()
