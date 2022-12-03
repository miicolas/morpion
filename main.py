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

    def __str__(self) -> str:
        strBoard = "-------------\n"
        for row in self.slots:
            for col in row:
                if col == 1:
                    strBoard += "| X "
                elif col == 2:
                    strBoard += "| O "
                else:
                    strBoard += "|   "
            strBoard += "|\n-------------\n"
        return strBoard

    def placeCross(self, col, row):
        self.slots[row - 1][col - 1] = 1

    def placeCircle(self, col, row):
        self.slots[row - 1][col - 1] = 2


board = Board()

window = pg.display.set_mode((600, 600))
pg.draw.rect(window, (255, 255, 255), pg.Rect(0, 196, 600, 8))
pg.draw.rect(window, (255, 255, 255), pg.Rect(0, 396, 600, 8))
pg.draw.rect(window, (255, 255, 255), pg.Rect(196, 0, 8, 600))
pg.draw.rect(window, (255, 255, 255), pg.Rect(396, 0, 8, 600))
pg.display.flip()
run = True
while run:
    leftClick = False

    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(f"left click at pos {pg.mouse.get_pos()}")

    for event in event_list:
        if event.type == pg.QUIT:
            pg.quit()
            running = False
