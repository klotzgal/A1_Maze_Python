from maze import Maze, Cell
from collections import deque


def bfs(maze: Maze, s: Cell, t: Cell):
    INF: int = 10 ** 9
    dist: list[list[int]] = [[INF] * maze.rows for _ in range(maze.cols)]
    q: deque = deque()
    dist[s.x][s.y] = 0
    q.append(s)

    while q:
        v: Cell = q.pop()
        for key, value in v.walls:
            if dist[v.x][v.y] != INF:
                if value:
                    pass
