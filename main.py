from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame as pg


class Board:
    """Game board"""

    def __init__(self) -> None:
        # Initialization of slots that serve as a box for the game with their coordinates
        self.player = 1  # 1 = Cross, 2 = Circle
        self.slots = [
            [0, 0, 0],  # (0, 0), (0, 1), (0, 2)
            [0, 0, 0],  # (1, 0), (1, 1), (1, 2)
            [0, 0, 0],  # (2, 0), (2, 1), (2, 2)
        ]  # 0 = Empty, 1 = Cross, 2 = Circle
        self.gameEnded = False

    def isSlotEmpty(self, row, col):
        if self.slots[row][col] == 0:
            return True
        return False

    def updateSlot(self, row, col, player):
        self.slots[row][col] = player

    def getClickedCase(self, pos):
        # When clicking on one of the boxes, we seek the horizontal and vertical coordinates of the corresponding box
        row = pos[1] // 200
        col = pos[0] // 200
        if 0 <= row <= 2 and 0 <= col <= 2:
            return (row, col)
        return False

    def setPlayer(self, player):
        self.player = player

    def getPlayer(self):
        return self.player

    def hasPlayerWon(self, pos):
        # The player wins when a column or a row or a diagonal is completed
        if (
            self.isRowComplete(pos[0])
            or self.isColComplete(pos[1])
            or self.isDiagComplete(pos)
        ):
            self.gameEnded = True  # The variable determines if the game is over
            return True

    def isRowComplete(self, row):
        # The line is complete when box 0, 1, 2 in x are filled
        if min(self.slots[row]) == max(self.slots[row]):
            pg.draw.line(
                window,
                (255, 255, 255),
                (30, 100 + 200 * row),
                (570, 100 + 200 * row),
                8,
            )
            return True
        return False

    def isColComplete(self, col):
        # The column is complete when the box 0, 1, 2 in it are filled
        colList = [self.slots[0][col], self.slots[1][col], self.slots[2][col]]
        if min(colList) == max(colList):
            pg.draw.line(
                window,
                (255, 255, 255),
                (100 + 200 * col, 30),
                (100 + 200 * col, 570),
                8,
            )
            return True
        return False

    def isDiagComplete(self, pos):
        # Check if one of the diagonal is completed
        self.diag1 = [
            self.slots[0][0],
            self.slots[1][1],
            self.slots[2][2],
        ]  # Determine the coordinates of diagonal 1
        self.diag2 = [
            self.slots[2][0],
            self.slots[1][1],
            self.slots[0][2],
        ]  # Determine the coordinates of diagonal 2
        if (pos[0], pos[1]) in [(0, 0), (1, 1), (2, 2)]:
            if min(self.diag1) == max(self.diag1):
                pg.draw.line(window, (255, 255, 255), (30, 30), (570, 570), 12)
                return True
        elif (pos[0], pos[1]) in [(2, 0), (1, 1), (0, 2)]:
            if min(self.diag2) == max(self.diag2):
                pg.draw.line(window, (255, 255, 255), (30, 570), (570, 30), 12)
                return True
        return False

    def isBoardComplete(self):
        for line in self.slots:
            for element in line:
                if element == 0:
                    return False
        self.gameEnded = True
        return True

    def placeCross(self, pos):
        # Placement of the cross with coordinates in pixels and position in x and y
        self.color = (255, 0, 0)
        if self.isSlotEmpty(pos[0], pos[1]):
            pg.draw.line(
                window,
                self.color,
                (45 + 200 * pos[1], 45 + 200 * pos[0]),
                (155 + 200 * pos[1], 155 + 200 * pos[0]),
                12,
            )
            pg.draw.line(
                window,
                self.color,
                (45 + 200 * pos[1], 155 + 200 * pos[0]),
                (155 + 200 * pos[1], 45 + 200 * pos[0]),
                12,
            )
            self.updateSlot(pos[0], pos[1], self.player)
            self.setPlayer(2)
            self.drawPlayerMark(self.getPlayer())

    def placeCircle(self, pos):
        # Placement of the circle with coordinates in pixels and position in x and y
        self.color = (0, 255, 0)
        if self.isSlotEmpty(pos[0], pos[1]):
            pg.draw.circle(
                window, (0, 255, 0), (100 + 200 * pos[1], 100 + 200 * pos[0]), 60, 8
            )
            self.updateSlot(pos[0], pos[1], self.player)
            self.setPlayer(1)
            self.drawPlayerMark(self.getPlayer())

    def drawGrid(self, color):
        # drawing the grid for game
        pg.draw.rect(window, color, pg.Rect(0, -4, 600, 8))
        pg.draw.rect(window, color, pg.Rect(0, 196, 600, 8))
        pg.draw.rect(window, color, pg.Rect(0, 396, 600, 8))
        pg.draw.rect(window, color, pg.Rect(0, 596, 600, 8))
        pg.draw.rect(window, color, pg.Rect(-1, 0, 8, 600))
        pg.draw.rect(window, color, pg.Rect(196, 0, 8, 600))
        pg.draw.rect(window, color, pg.Rect(396, 0, 8, 600))
        pg.draw.rect(window, color, pg.Rect(596, 0, 8, 600))
        pg.display.flip()

    def drawPlayerMark(self, player):
        pg.draw.rect(
            window, (255, 0, 0) if player == 1 else (0, 255, 0), pg.Rect(196, 196, 8, 8)
        )
        pg.draw.rect(
            window, (255, 0, 0) if player == 1 else (0, 255, 0), pg.Rect(396, 196, 8, 8)
        )
        pg.draw.rect(
            window, (255, 0, 0) if player == 1 else (0, 255, 0), pg.Rect(196, 396, 8, 8)
        )
        pg.draw.rect(
            window, (255, 0, 0) if player == 1 else (0, 255, 0), pg.Rect(396, 396, 8, 8)
        )
        pg.display.flip()

    def handleWin(self, player):
        color = (255, 0, 0) if player == 1 else (0, 255, 0)
        for i in range(5):  # Blinking line
            self.drawGrid(color)
            pg.time.wait(200)
            self.drawGrid((255, 255, 255))
            pg.time.wait(200)
        pg.draw.rect(window, (0, 0, 0), pg.Rect(0, 0, 600, 600))
        if player == 1:  # Victory message for the cross
            winText = font.render("Cross Wins !", True, (255, 0, 0))
            window.blit(winText, (40, 80))
            winText = font.render("Press Return", True, (255, 0, 0))
            window.blit(winText, (40, 240))
            winText = font.render("to play again", True, (255, 0, 0))
            window.blit(winText, (45, 320))
            pg.display.flip()
        elif player == 2:  # Victory message for the circle
            winText = font.render("Circle Wins !", True, (0, 255, 0))
            window.blit(winText, (40, 80))
            winText = font.render("Press Return", True, (0, 255, 0))
            window.blit(winText, (40, 240))
            winText = font.render("to play again", True, (0, 255, 0))
            window.blit(winText, (45, 320))
            pg.display.flip()

    def handleDraw(self):
        print("Draw")
        pg.draw.rect(window, (0, 0, 0), pg.Rect(0, 0, 600, 600))
        winText = font.render("It's a draw !", True, (255, 255, 0))
        window.blit(winText, (80, 80))
        winText = font.render("Press Return", True, (255, 255, 0))
        window.blit(winText, (40, 240))
        winText = font.render("to play again", True, (255, 255, 0))
        window.blit(winText, (45, 320))
        pg.display.flip()


board = Board()
pg.init()
font = pg.font.Font(None, 120)
window = pg.display.set_mode((600, 600))
pg.display.set_caption("Tic Tac Toe")
board.drawGrid((255, 255, 255))
run = True
board.drawPlayerMark(board.player)

while run:
    event_list = pg.event.get()
    for event in event_list:
        if not board.gameEnded:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = board.getClickedCase(pg.mouse.get_pos())
                    if board.getPlayer() == 1 and pos:
                        board.placeCross(pos)
                        if board.hasPlayerWon(pos):
                            print("Cross Wins")
                            board.handleWin(1)
                        elif board.isBoardComplete():
                            board.handleDraw()
                    elif board.getPlayer() == 2 and pos:
                        board.placeCircle(pos)
                        if board.hasPlayerWon(pos):
                            print("Circle Wins")
                            board.handleWin(2)
                        elif board.isBoardComplete():
                            board.handleDraw()
                    else:
                        pass
        else:
            if event.type == pg.KEYDOWN:
                if (
                    event.key == pg.K_RETURN
                ):  # if the return key is pressed then we create a new game board
                    board = Board()
                    pg.draw.rect(window, (0, 0, 0), pg.Rect(0, 0, 600, 600))
                    board.drawGrid((255, 255, 255))
                    board.drawPlayerMark(board.getPlayer())

    for event in event_list:
        if event.type == pg.QUIT:
            pg.quit()
            running = False
            exit(-1)
    pg.display.flip()
