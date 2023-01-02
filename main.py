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
        col = (pos[0] - 300) // 200
        if 0 <= row <= 2 and 0 <= col <= 2:
            return (row, col)
        return False

    def setPlayer(self, player):
        self.player = player

    def getPlayer(self):
        return self.player

    def hasPlayerWon(self, pos):
        if (
            self.isRowComplete(pos[0])
            or self.isColComplete(pos[1])
            or self.isDiagComplete(pos)
        ):
            return True
            self.gameEnded = True

    def isRowComplete(self, row):
        # The line is complete when box 0, 1, 2 in x are filled
        if min(self.slots[row]) == max(self.slots[row]):
            pg.draw.line(
                window,
                (255, 255, 255),
                (330, 100 + 200 * row),
                (870, 100 + 200 * row),
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
                (400 + 200 * col, 30),
                (400 + 200 * col, 570),
                8,
            )
            return True
        return False

    def isDiagComplete(self, pos):
        print(pos)
        self.diag1 = [self.slots[0][0], self.slots[1][1], self.slots[2][2]]
        self.diag2 = [self.slots[2][0], self.slots[1][1], self.slots[0][2]]
        if (pos[0], pos[1]) in [(0, 0), (1, 1), (2, 2)]:
            if min(self.diag1) == max(self.diag1):
                pg.draw.line(window, (255, 255, 255), (330, 30), (870, 570), 12)
                return True
        elif (pos[0], pos[1]) in [(2, 0), (1, 1), (0, 2)]:
            print("diag2", self.diag2)
            if min(self.diag2) == max(self.diag2):
                pg.draw.line(window, (255, 255, 255), (330, 570), (870, 30), 12)
                return True
        return False

    def placeCross(self, pos):
        # Placement of the cross with coordinates in pixels and position in x and y
        self.color = (255, 0, 0)
        if self.isSlotEmpty(pos[0], pos[1]):
            pg.draw.line(
                window,
                self.color,
                (345 + 200 * pos[1], 45 + 200 * pos[0]),
                (455 + 200 * pos[1], 155 + 200 * pos[0]),
                12,
            )
            pg.draw.line(
                window,
                self.color,
                (345 + 200 * pos[1], 155 + 200 * pos[0]),
                (455 + 200 * pos[1], 45 + 200 * pos[0]),
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
                window, (0, 255, 0), (400 + 200 * pos[1], 100 + 200 * pos[0]), 60, 8
            )
            self.updateSlot(pos[0], pos[1], self.player)
            self.setPlayer(1)
            self.drawPlayerMark(self.getPlayer())

    def drawGrid(self, color):
        # drawing the grid for game
        pg.draw.rect(window, color, pg.Rect(300, -4, 600, 8))
        pg.draw.rect(window, color, pg.Rect(300, 196, 600, 8))
        pg.draw.rect(window, color, pg.Rect(300, 396, 600, 8))
        pg.draw.rect(window, color, pg.Rect(300, 596, 600, 8))
        pg.draw.rect(window, color, pg.Rect(296, 0, 8, 600))
        pg.draw.rect(window, color, pg.Rect(496, 0, 8, 600))
        pg.draw.rect(window, color, pg.Rect(696, 0, 8, 600))
        pg.draw.rect(window, color, pg.Rect(896, 0, 8, 600))
        pg.display.flip()

    def drawPlayerMark(self, player):
        pg.draw.rect(
            window, (255, 0, 0) if player == 1 else (0, 255, 0), pg.Rect(496, 196, 8, 8)
        )
        pg.draw.rect(
            window, (255, 0, 0) if player == 1 else (0, 255, 0), pg.Rect(696, 196, 8, 8)
        )
        pg.draw.rect(
            window, (255, 0, 0) if player == 1 else (0, 255, 0), pg.Rect(496, 396, 8, 8)
        )
        pg.draw.rect(
            window, (255, 0, 0) if player == 1 else (0, 255, 0), pg.Rect(696, 396, 8, 8)
        )
        pg.display.flip()

    def handleWin(self, player):
        color = (255, 0, 0) if player == 1 else (0, 255, 0)
        for i in range(5):
            self.drawGrid(color)
            pg.time.wait(200)
            self.drawGrid((255, 255, 255))
            pg.time.wait(200)


board = Board()
window = pg.display.set_mode((1200, 600))
board.drawGrid((255, 255, 255))
run = True
board.drawPlayerMark(board.player)

while run:
    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if not board.gameEnded:
                    pos = board.getClickedCase(pg.mouse.get_pos())
                    if board.getPlayer() == 1 and pos:
                        board.placeCross(pos)
                        if board.hasPlayerWon(pos):
                            print("Cross Wins")
                            board.handleWin(1)
                    elif board.getPlayer() == 2 and pos:
                        board.placeCircle(pos)
                        if board.hasPlayerWon(pos):
                            print("Circle Wins")
                            board.handleWin(2)
                    else:
                        pass

    for event in event_list:
        if event.type == pg.QUIT:
            pg.quit()
            running = False
            exit(-1)
    pg.display.flip()
