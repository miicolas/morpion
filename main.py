import numpy as np
import pygame as pg


class Board:
    """Game board"""

    def __init__(self) -> None:
        self.slots = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]  # 0 = Empty, 1 = Cross, 2 = Circle

    def placeCross(self, pos):
        self.color = (255, 0, 0)
        if pos[0] < 196:
            if pos[1] < 196:
                if self.slots[0][0] == 0:
                    pg.draw.line(window, self.color, (45, 45), (155, 155), 12)
                    pg.draw.line(window, self.color, (45, 155), (155, 45), 12)
                    self.slots[0][0] = 1
            if 204 < pos[1] < 396:
                if self.slots[1][0] == 0:
                    pg.draw.line(window, self.color, (45, 245), (155, 355), 12)
                    pg.draw.line(window, self.color, (45, 355), (155, 245), 12)
                    self.slots[1][0] = 1
            if 404 < pos[1]:
                if self.slots[2][0] == 0:
                    pg.draw.line(window, self.color, (45, 445), (155, 555), 12)
                    pg.draw.line(window, self.color, (45, 555), (155, 445), 12)
                    self.slots[2][0] = 1
            else:
                pass
        elif 204 < pos[0] < 396:
            if pos[1] < 196:
                if self.slots[0][1] == 0:
                    pg.draw.line(window, self.color, (245, 45), (355, 155), 12)
                    pg.draw.line(window, self.color, (245, 155), (355, 45), 12)
                    self.slots[0][1] = 1
            if 204 < pos[1] < 396:
                if self.slots[1][1] == 0:
                    pg.draw.line(window, self.color, (245, 245), (355, 355), 12)
                    pg.draw.line(window, self.color, (245, 355), (355, 245), 12)
                    self.slots[1][1] = 1
            if 404 < pos[1]:
                if self.slots[2][1] == 0:
                    pg.draw.line(window, self.color, (245, 445), (355, 555), 12)
                    pg.draw.line(window, self.color, (245, 555), (355, 445), 12)
                    self.slots[2][1] = 1
            else:
                pass
        elif 404 < pos[0]:
            if pos[1] < 196:
                if self.slots[0][2] == 0:
                    pg.draw.line(window, self.color, (445, 45), (555, 155), 12)
                    pg.draw.line(window, self.color, (445, 155), (555, 45), 12)
                    self.slots[0][2] = 1
            if 204 < pos[1] < 396:
                if self.slots[1][2] == 0:
                    pg.draw.line(window, self.color, (445, 245), (555, 355), 12)
                    pg.draw.line(window, self.color, (445, 355), (555, 245), 12)
                    self.slots[1][2] = 1
            if 404 < pos[1]:
                if self.slots[2][2] == 0:
                    pg.draw.line(window, self.color, (445, 445), (555, 555), 12)
                    pg.draw.line(window, self.color, (445, 555), (555, 445), 12)
                    self.slots[2][2] = 1
            else:
                pass
        else:
            pass

    def placeCircle(self, pos):
        if pos[0] < 196:
            if pos[1] < 196:
                if self.slots[0][0] == 0:
                    pg.draw.circle(window, (0, 255, 0), (100, 100), 60, 8)
                    self.slots[0][0] = 2
            if 204 < pos[1] < 396:
                if self.slots[1][0] == 0:
                    pg.draw.circle(window, (0, 255, 0), (100, 300), 60, 8)
                    self.slots[1][0] = 2
            if 404 < pos[1]:
                if self.slots[2][0] == 0:
                    pg.draw.circle(window, (0, 255, 0), (100, 500), 60, 8)
                    self.slots[2][0] = 2
            else:
                pass
        elif 204 < pos[0] < 396:
            if pos[1] < 196:
                if self.slots[0][1] == 0:
                    pg.draw.circle(window, (0, 255, 0), (300, 100), 60, 8)
                    self.slots[0][1] = 2
            if 204 < pos[1] < 396:
                if self.slots[1][1] == 0:
                    pg.draw.circle(window, (0, 255, 0), (300, 300), 60, 8)
                    self.slots[1][1] = 2
            if 404 < pos[1]:
                if self.slots[2][1] == 0:
                    pg.draw.circle(window, (0, 255, 0), (300, 500), 60, 8)
                    self.slots[2][1] = 2
            else:
                pass
        elif 404 < pos[0]:
            if pos[1] < 196:
                if self.slots[0][2] == 0:
                    pg.draw.circle(window, (0, 255, 0), (500, 100), 60, 8)
                    self.slots[0][2] = 2
            if 204 < pos[1] < 396:
                if self.slots[1][2] == 0:
                    pg.draw.circle(window, (0, 255, 0), (500, 300), 60, 8)
                    self.slots[1][2] = 2
            if 404 < pos[1]:
                if self.slots[2][2] == 0:
                    pg.draw.circle(window, (0, 255, 0), (500, 500), 60, 8)
                    self.slots[2][2] = 2
            else:
                pass
        else:
            pass

    def drawGrid(self, color):
        pg.draw.rect(window, color, pg.Rect(0, 196, 600, 8))
        pg.draw.rect(window, color, pg.Rect(0, 396, 600, 8))
        pg.draw.rect(window, color, pg.Rect(196, 0, 8, 600))
        pg.draw.rect(window, color, pg.Rect(396, 0, 8, 600))
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


board = Board()

window = pg.display.set_mode((600, 600))
board.drawGrid((255, 255, 255))
run = True
player = 1
board.drawPlayerMark(1)
while run:
    leftClick = False

    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pg.mouse.get_pos()
                if player == 1:
                    board.placeCross(pos)
                    board.drawPlayerMark(2)
                else:
                    board.placeCircle(pos)
                    board.drawPlayerMark(1)
                player = 2 if player == 1 else 1

    for event in event_list:
        if event.type == pg.QUIT:
            pg.quit()
            running = False
    pg.display.flip()
