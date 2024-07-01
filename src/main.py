from maze import Maze, Cell
from algorithm import bfs
from load import Loader
import os

if __name__ == '__main__':
    l = Loader()
    dir = os.path.abspath('.')
    file = 'files/1.txt'
    if not dir.endswith('/src'):
        file = 'src/' + file
    m = l.download(file)
    bfs(m, Cell(0, 0),  Cell(2, 2))
    m.print('top')
