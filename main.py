import sys
from data.classChessBoard.mainChessBoadFile import *

from data.classChessBoard.mainChessBoadFile import ChessBoard
from data.classFigure.queen import queenFigure
from data.classFigure.king import kingFigure
from data.classFigure.bishop import bishopFigure
from data.classFigure.knight import knightFigure
from data.classFigure.pawn import pawnFigure
from data.classFigure.rook import rookFigure



from data.classChessBoard.mainChessBoadFile import LISTOFLETTERS
from data.classChessBoard.mainChessBoadFile import LISTOFNUMBER

# Инициализация окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Шахматная доска")


# Создание клеток шахматной доски 
listOfCells = ChessBoard.creatingCellsDesc()

# Create figure queen for the board
queenW = queenFigure.createFigure(x_position= "D", y_position= "1", imageObject= "data/classFigure/Image/wQ.svg")

kingW = kingFigure.createFigure(x_position= "E", y_position= "1", imageObject= "data/classFigure/Image/wK.svg")

bishopW_L = bishopFigure.createFigure(x_position= "C", y_position= "1", imageObject= "data/classFigure/Image/wB.svg")
bishopW_R = bishopFigure.createFigure(x_position= "F", y_position= "1", imageObject= "data/classFigure/Image/wB.svg")

knightW_L = knightFigure.createFigure(x_position= "B", y_position= "1", imageObject= "data/classFigure/Image/wN.svg")
knightW_R = knightFigure.createFigure(x_position= "G", y_position= "1", imageObject= "data/classFigure/Image/wN.svg")

rookW_L = rookFigure.createFigure(x_position= "A", y_position= "1", imageObject= "data/classFigure/Image/wR.svg")
rookW_R = rookFigure.createFigure(x_position= "H", y_position= "1", imageObject= "data/classFigure/Image/wR.svg")

queenB = queenFigure.createFigure(x_position= "D", y_position= "9", imageObject= "data/classFigure/Image/bQ.svg")

kingB = kingFigure.createFigure(x_position= "E", y_position= "9", imageObject= "data/classFigure/Image/bK.svg")

bishopB_L = bishopFigure.createFigure(x_position= "C", y_position= "9", imageObject= "data/classFigure/Image/bB.svg")
bishopB_R = bishopFigure.createFigure(x_position= "F", y_position= "9", imageObject= "data/classFigure/Image/bB.svg")

knightB_L = knightFigure.createFigure(x_position= "B", y_position= "9", imageObject= "data/classFigure/Image/bN.svg")
knightB_R = knightFigure.createFigure(x_position= "G", y_position= "9", imageObject= "data/classFigure/Image/bN.svg")

rookB_L = rookFigure.createFigure(x_position= "A", y_position= "9", imageObject= "data/classFigure/Image/bR.svg")
rookB_R = rookFigure.createFigure(x_position= "H", y_position= "9", imageObject= "data/classFigure/Image/bR.svg")


pawnW_List = [pawnFigure.createFigure(x_position= LISTOFLETTERS[i], y_position= "2", imageObject= "data/classFigure/Image/wP.svg") for i in range(8)]
pawnB_List = [pawnFigure.createFigure(x_position= LISTOFLETTERS[i], y_position= "8", imageObject= "data/classFigure/Image/bP.svg") for i in range(8)]




# Главный цикл программы
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)


    # Отрисовка клеток шахматной доски
    for cell in listOfCells: cell.draw(screen)


    # Отрисовка линий для разделения пространства счетчика времени
    pygame.draw.line(screen, BLACK, (48, 48), (48, 771), 2)  # Левая граница
    pygame.draw.line(screen, BLACK, (690, 48), (690, 770), 2)  # Правая граница
    pygame.draw.line(screen, BLACK, (50, 48), (690, 48), 2)  # Верх граница
    pygame.draw.line(screen, BLACK, (50, 770), (690, 770), 2)  # Нижняя граница

    ChessBoard.drawCellsNumerated(surface= screen, list= listOfCells)


    # Draw the queen figure 
    queenW.draw(screen)
    queenB.draw(screen)

    kingW.draw(screen)
    kingB.draw(screen)
    
    bishopW_L.draw(screen)
    bishopW_R.draw(screen)

    bishopB_L.draw(screen)
    bishopB_R.draw(screen)

    knightW_L.draw(screen)
    knightW_R.draw(screen)

    knightB_L.draw(screen)
    knightB_R.draw(screen)

    rookW_L.draw(screen)
    rookW_R.draw(screen)

    rookB_L.draw(screen)
    rookB_R.draw(screen)


    for pawnW in pawnW_List: pawnW.draw(screen)
    for pawnB in pawnB_List: pawnB.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

# Завершение программы
pygame.quit()
sys.exit()
