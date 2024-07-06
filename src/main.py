from maze import Maze, Cell
from algorithm import bfs, get_path, is_perfect_maze
from load import Loader
import os

if __name__ == '__main__':
    l = Loader()
    file = 'files/1.txt'
    m = l.download(file)
    frm: list[list[tuple[int, int]]] = bfs(m, (0, 0))
    is_prf_maze = is_perfect_maze(frm)
    path: list[tuple[int, int]] = get_path(frm, (5, 5))
    m.print('top')
