import pygame as pg


class Board:
    """Game board"""

    def __init__(self) -> None:
        self.player = 1  # 1 = Cross, 2 = Circle
        self.slots = [
            [0, 0, 0],  # (0, 0), (0, 1), (0, 2)
            [0, 0, 0],  # (1, 0), (1, 1), (1, 2)
            [0, 0, 0],  # (2, 0), (2, 1), (2, 2)
        ]  # 0 = Empty, 1 = Cross, 2 = Circle

    def isSlotEmpty(self, row, col):
        if self.slots[row][col] == 0:
            return True
        return False

    def updateSlot(self, row, col, player):
        self.slots[row][col] = player

    def getClickedCase(self, pos):
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
        if self.isRowComplete(pos[0]) or self.isColComplete(pos[1]):
            return True

    def isRowComplete(self, row):
        if min(self.slots[row]) == max(self.slots[row]):
            return True
        return False

    def isColComplete(self, col):
        col = [self.slots[0][col], self.slots[1][col], self.slots[2][col]]
        if min(col) == max(col):
            return True
        return False

    def placeCross(self, pos):
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
        self.color = (0, 255, 0)
        if self.isSlotEmpty(pos[0], pos[1]):
            pg.draw.circle(
                window, (0, 255, 0), (400 + 200 * pos[1], 100 + 200 * pos[0]), 60, 8
            )
            self.updateSlot(pos[0], pos[1], self.player)
            self.setPlayer(1)
            self.drawPlayerMark(self.getPlayer())

    def drawGrid(self, color):
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
                pos = board.getClickedCase(pg.mouse.get_pos())
                if board.getPlayer() == 1 and pos:
                    board.placeCross(pos)
                    if board.hasPlayerWon(pos):
                        print("Cross Wins")
                elif board.getPlayer() == 2 and pos:
                    board.placeCircle(pos)
                    if board.hasPlayerWon(pos):
                        print("Circle Wins")
                else:
                    pass

    for event in event_list:
        if event.type == pg.QUIT:
            pg.quit()
            running = False
            exit(-1)
    pg.display.flip()
