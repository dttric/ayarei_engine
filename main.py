import pygame as pg
from settings import *
from player import Player
import math as m
from map import world_map
from drawing import Drawing
from tkinter import messagebox
messagebox.showinfo('я забил на поддержку и удалил описание\nключи блоков остались в игре')
pg.init()
dis = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("аярей енжин")
clock = pg.time.Clock()
player = Player()
drawing = Drawing(dis)


while True:
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        exit()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    player.movement()
    dis.fill(BLACK)
    drawing.background(player.angle)
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    pg.display.flip()
    clock.tick()
