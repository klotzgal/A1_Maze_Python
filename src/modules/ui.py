import easygui
import pygame
from pygame.draw import line
from pygame.surface import Surface

from modules.algorithm import bfs, get_path
from modules.load import Loader
from modules.maze import Cell, Maze


class UI:
    def __init__(self) -> None:
        pass

    def main_loop(self) -> None:
        pygame.init()
        screen: Surface = pygame.display.set_mode((502, 502))
        file = 'tests/files/3.txt'
        try:
            loader = Loader()
            maze = loader.download(file)
            self._draw_maze(screen, maze)
            frm = bfs(maze, (2, 3))
            path = get_path(frm, (16, 10))
            STEP = 500 / max(maze.cols, maze.rows)
            self._draw_path(screen, path, STEP)
        except Exception as e:
            easygui.msgbox(e)

        is_running = True
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
            pygame.display.flip()
        pygame.quit()

    def _draw_maze(self, screen: Surface, maze: Maze) -> None:
        STEP = 500 / max(maze.cols, maze.rows)
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

    def _draw_path(
        self, screen: Surface, path: list[tuple[int, int]], STEP: float
    ) -> None:
        for i in range(len(path) - 1):
            line(
                screen,
                (0, 255, 0),
                (path[i][0] * STEP + STEP / 2, path[i][1] * STEP + STEP / 2),
                (path[i + 1][0] * STEP + STEP / 2, path[i + 1][1] * STEP + STEP / 2),
            )
