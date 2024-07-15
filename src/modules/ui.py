import sys

import pygame
from pygame.draw import line
from pygame.surface import Surface

from modules.load import Loader
from modules.maze import Cell, Maze


def main_loop():
    pygame.init()
    screen: Surface = pygame.display.set_mode((1200, 1200))
    try:
        loader = Loader()
    except Exception as e:
        print(e)
    file = 'tests/files/1.txt'
    maze = loader.download(file)
    draw_maze(screen, maze)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()


def draw_maze(screen: Surface, maze: Maze):
    STEP = 10
    for y in range(maze.cols):
        for x in range(maze.rows):
            cell: Cell = maze.field[y][x]
            if cell.walls['top']:
                line(
                    screen,
                    (255, 0, 0),
                    (x * STEP, y * STEP),
                    ((x + 1) * STEP, y * STEP),
                    2,
                )
            if cell.walls['bottom']:
                line(
                    screen,
                    (255, 0, 0),
                    (x * STEP, (y + 1) * STEP),
                    ((x + 1) * STEP, (y + 1) * STEP),
                    2,
                )
            if cell.walls['right']:
                line(
                    screen,
                    (255, 0, 0),
                    ((x + 1) * STEP, y * STEP),
                    ((x + 1) * STEP, (y + 1) * STEP),
                    2,
                )
            if cell.walls['left']:
                line(
                    screen,
                    (255, 0, 0),
                    (x * STEP, y * STEP),
                    (x * STEP, (y + 1) * STEP),
                    2,
                )
