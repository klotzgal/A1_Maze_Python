from modules.algorithm import bfs, get_path, is_perfect_maze
from modules.load import Loader

if __name__ == '__main__':
    loader = Loader()
    file = 'files/1.txt'
    maze = loader.download(file)
    frm: list[list[tuple[int, int]]] = bfs(maze, (0, 0))
    is_prf_maze = is_perfect_maze(frm)
    path: list[tuple[int, int]] = get_path(frm, (5, 5))
    maze.print('top')
