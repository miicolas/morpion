import pygame as pg
import random


class Board:
    """Game board"""

    def __init__(self) -> None:
        self.slots = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]  # 0 = Empty, 1 = Cross, 2 = Circle

    def isSlotEmpty(self, row, col):
        if self.slots[row][col] == 0:
            return True
        return False

    def updateSlot(self, row, col, player):
        self.slots[row][col] = player

    def placeCross(self, pos):
        self.color = (255, 0, 0)
        if 304 < pos[0] < 496:
            if pos[1] < 196:
                if self.isSlotEmpty(0, 0):
                    pg.draw.line(window, self.color, (345, 45), (455, 155), 12)
                    pg.draw.line(window, self.color, (345, 155), (455, 45), 12)
                    self.updateSlot(0, 0, 1)
            if 204 < pos[1] < 396:
                if self.isSlotEmpty(1, 0):
                    pg.draw.line(window, self.color, (345, 245), (455, 355), 12)
                    pg.draw.line(window, self.color, (345, 355), (455, 245), 12)
                    self.updateSlot(1, 0, 1)
            if 404 < pos[1]:
                if self.isSlotEmpty(2, 0):
                    pg.draw.line(window, self.color, (345, 445), (455, 555), 12)
                    pg.draw.line(window, self.color, (345, 555), (455, 445), 12)
                    self.updateSlot(2, 0, 1)
            else:
                pass
        elif 504 < pos[0] < 696:
            if pos[1] < 196:
                if self.isSlotEmpty(0, 1):
                    pg.draw.line(window, self.color, (545, 45), (655, 155), 12)
                    pg.draw.line(window, self.color, (545, 155), (655, 45), 12)
                    self.updateSlot(0, 1, 1)
            if 204 < pos[1] < 396:
                if self.isSlotEmpty(1, 1):
                    pg.draw.line(window, self.color, (545, 245), (655, 355), 12)
                    pg.draw.line(window, self.color, (545, 355), (655, 245), 12)
                    self.updateSlot(1, 1, 1)
            if 404 < pos[1]:
                if self.isSlotEmpty(2, 1):
                    pg.draw.line(window, self.color, (545, 445), (655, 555), 12)
                    pg.draw.line(window, self.color, (545, 555), (655, 445), 12)
                    self.updateSlot(2, 1, 1)
            else:
                pass
        elif 704 < pos[0] < 896:
            if pos[1] < 196:
                if self.isSlotEmpty(0, 2):
                    pg.draw.line(window, self.color, (745, 45), (855, 155), 12)
                    pg.draw.line(window, self.color, (745, 155), (855, 45), 12)
                    self.updateSlot(0, 2, 1)
            if 204 < pos[1] < 396:
                if self.isSlotEmpty(1, 2):
                    pg.draw.line(window, self.color, (745, 245), (855, 355), 12)
                    pg.draw.line(window, self.color, (745, 355), (855, 245), 12)
                    self.updateSlot(1, 2, 1)
            if 404 < pos[1]:
                if self.isSlotEmpty(2, 2):
                    pg.draw.line(window, self.color, (745, 445), (855, 555), 12)
                    pg.draw.line(window, self.color, (745, 555), (855, 445), 12)
                    self.updateSlot(2, 2, 1)
            else:
                pass
        else:
            pass

    def placeCircle(self, pos):
        if 304 < pos[0] < 496:
            if pos[1] < 196:
                if self.isSlotEmpty(0, 0):
                    pg.draw.circle(window, (0, 255, 0), (400, 100), 60, 8)
                    self.updateSlot(0, 0, 2)
            if 204 < pos[1] < 396:
                if self.isSlotEmpty(1, 0):
                    pg.draw.circle(window, (0, 255, 0), (400, 300), 60, 8)
                    self.updateSlot(1, 0, 2)
            if 404 < pos[1]:
                if self.isSlotEmpty(2, 0):
                    pg.draw.circle(window, (0, 255, 0), (400, 500), 60, 8)
                    self.updateSlot(2, 0, 2)
            else:
                pass
        elif 504 < pos[0] < 696:
            if pos[1] < 196:
                if self.isSlotEmpty(0, 1):
                    pg.draw.circle(window, (0, 255, 0), (600, 100), 60, 8)
                    self.updateSlot(0, 1, 2)
            if 204 < pos[1] < 396:
                if self.isSlotEmpty(1, 1):
                    pg.draw.circle(window, (0, 255, 0), (600, 300), 60, 8)
                    self.updateSlot(1, 1, 2)
            if 404 < pos[1]:
                if self.isSlotEmpty(2, 1):
                    pg.draw.circle(window, (0, 255, 0), (600, 500), 60, 8)
                    self.updateSlot(2, 1, 2)
            else:
                pass
        elif 704 < pos[0] < 896:
            if pos[1] < 196:
                if self.isSlotEmpty(0, 2):
                    pg.draw.circle(window, (0, 255, 0), (800, 100), 60, 8)
                    self.updateSlot(0, 2, 2)
            if 204 < pos[1] < 396:
                if self.isSlotEmpty(1, 2):
                    pg.draw.circle(window, (0, 255, 0), (800, 300), 60, 8)
                    self.updateSlot(1, 2, 2)
            if 404 < pos[1]:
                if self.isSlotEmpty(2, 2):
                    pg.draw.circle(window, (0, 255, 0), (800, 500), 60, 8)
                    self.updateSlot(2, 2, 2)
            else:
                pass
        else:
            pass

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


def main():
    board = Board()
    window = pg.display.set_mode((1200, 600))
    board.drawGrid((255, 255, 255))
    run = True
    player = random.randint(1,2)
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
                    # ! Ici on peut afficher la couleur du joueur soit avec les petits carrés soit avec toute la grille colorée

        for event in event_list:
            if event.type == pg.QUIT:
                pg.quit()
                running = False
        pg.display.flip()
