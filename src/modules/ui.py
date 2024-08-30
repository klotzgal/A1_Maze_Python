import pygame
from pygame.draw import line
from pygame.surface import Surface

from modules.algorithm import bfs, get_path
from modules.load import Loader
from modules.maze import Cell, Maze


class UI:
    def __init__(self) -> None:
        pygame.init()
        self.screen: Surface = pygame.display.set_mode((502, 502))
        self.file: str = None
        self.maze: Maze = None
        self.path: list[tuple[int, int]] = None
        self.STEP: int = None

    def main_loop(self) -> None:
        file = 'tests/files/3.txt'
        self.push_button_load_file(file)
        self.push_button_path()

        is_running = True
        is_show_path = False
        while is_running:
            self._draw_maze()
            if is_show_path:
                self._draw_path()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_show_path = not is_show_path
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    is_show_path = not is_show_path

            pygame.display.flip()
        pygame.quit()

    def push_button_path(self):
        frm: list[list[tuple[int, int]]] = bfs(self.maze, (2, 3))
        self.path: list[tuple[int, int]] = get_path(frm, (16, 10))

    def push_button_load_file(self, file):
        try:
            self.maze: Maze = Loader().download(file)
            self.STEP: int = 500 / max(self.maze.cols, self.maze.rows)
        except Exception as e:
            print(e)

    def _draw_maze(self) -> None:
        if self.maze is None:
            return

        color: tuple[int, int, int] = (255, 0, 0)
        for y in range(self.maze.cols):
            for x in range(self.maze.rows):
                cell: Cell = self.maze.field[y][x]
                if cell.walls['top']:
                    line(
                        self.screen,
                        color,
                        (x * self.STEP, y * self.STEP),
                        ((x + 1) * self.STEP, y * self.STEP),
                        2,
                    )
                if cell.walls['bottom']:
                    line(
                        self.screen,
                        color,
                        (x * self.STEP, (y + 1) * self.STEP),
                        ((x + 1) * self.STEP, (y + 1) * self.STEP),
                        2,
                    )
                if cell.walls['right']:
                    line(
                        self.screen,
                        color,
                        ((x + 1) * self.STEP, y * self.STEP),
                        ((x + 1) * self.STEP, (y + 1) * self.STEP),
                        2,
                    )
                if cell.walls['left']:
                    line(
                        self.screen,
                        color,
                        (x * self.STEP, y * self.STEP),
                        (x * self.STEP, (y + 1) * self.STEP),
                        2,
                    )

    def _draw_path(self) -> None:
        if self.path is None:
            return

        color: tuple[int, int, int] = (0, 255, 0)
        for i in range(len(self.path) - 1):
            line(
                self.screen,
                color,
                (
                    self.path[i][0] * self.STEP + self.STEP / 2,
                    self.path[i][1] * self.STEP + self.STEP / 2,
                ),
                (
                    self.path[i + 1][0] * self.STEP + self.STEP / 2,
                    self.path[i + 1][1] * self.STEP + self.STEP / 2,
                ),
            )
