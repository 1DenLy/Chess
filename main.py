import sys
from data.classChessBoard.mainChessBoadFile import *
from data.classFigure import *

from data.classChessBoard.mainChessBoadFile import ChessBoard



# Создание клеток шахматной доски
listOfCells = ChessBoard.creatingCellsDesc()

# Инициализация окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Шахматная доска")


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



    ChessBoard.drawCellsNumerated(screen, listOfCells)

    # Отрисовка линий для разделения пространства счетчика времени
    pygame.draw.line(screen, BLACK, (50, 50), (50, 770), 2)  # Левая граница
    pygame.draw.line(screen, BLACK, (690, 50), (690, 770), 2)  # Правая граница
    pygame.draw.line(screen, BLACK, (50, 50), (690, 50), 2)  # Верх граница
    pygame.draw.line(screen, BLACK, (50, 770), (690, 770), 2)  # Нижняя граница
    

    pygame.display.flip()
    clock.tick(FPS)

# Завершение программы
pygame.quit()
sys.exit()
