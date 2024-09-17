import random
from typing import List
from maze import Maze, Cell


def display_maze(field: list[list[Cell]], rows, cols) -> None:
    """Display the maze in the terminal."""

    # Top border
    print("+" + "---+" * cols)

    for row in range(rows):
        # Display row
        row_cells = "|"
        for col in range(cols):
            cell = field[row][col]
            row_cells += "   "  # Cell content
            if cell.walls['right']:
                row_cells += "|"
            else:
                row_cells += " "

        print(row_cells)

        # Display bottom border
        if row == rows - 1:
            print("+" + "---+" * cols)
        else:
            bottom_border = "+"
            for col in range(cols):
                cell = field[row][col]
                if cell.walls['bottom']:
                    bottom_border += "---+"
                else:
                    bottom_border += "   +"
            print(bottom_border)


class MazeEller(Maze):
    def __init__(self, rows: int, cols: int) -> None:
        super().__init__(rows, cols)

    def __repr__(self) -> str:
        maze_str = ''
        for row in range(self.rows):
            # Верхние стены
            maze_str += '  '
            for col in range(self.cols):
                if self.field[row][col].walls['top']:
                    maze_str += '+-'
                else:
                    maze_str += '+ '
            maze_str += '+\n'

            # Левые стены и сами клетки
            for col in range(self.cols):
                if self.field[row][col].walls['left']:
                    maze_str += '| '
                else:
                    maze_str += '  '
            maze_str += '|\n'

        # Последняя строка с нижними стенами
        maze_str += '  '
        for col in range(self.cols):
            if self.field[self.rows - 1][col].walls['bottom']:
                maze_str += '+-'
            else:
                maze_str += '+ '
        maze_str += '+\n'

        return maze_str

    def generate(self) -> None:
        rows = self.rows
        cols = self.cols

        # Инициализация структур данных
        sets = list(range(cols))  # Наборы для объединения по строкам

        def find_set(sets, col):
            while sets[col] != col:
                col = sets[col]
            return col

        def union_sets(sets, col1, col2):
            root1 = find_set(sets, col1)
            root2 = find_set(sets, col2)
            if root1 != root2:
                sets[root2] = root1

        for row in range(rows):
            for col in range(cols):
                if col < cols - 1:
                    if find_set(sets, col) != find_set(sets, col + 1) and random.choice([True, False]):
                        self.field[row][col].walls['right'] = True
                        self.field[row][col + 1].walls['left'] = True
                        union_sets(sets, col, col + 1)

            if row < rows - 1:
                new_sets = list(range(cols))
                for col in range(cols):
                    if find_set(sets, col) != find_set(new_sets, col) and random.choice([True, False]):
                        self.field[row][col].walls['bottom'] = True
                        self.field[row + 1][col].walls['top'] = True
                        union_sets(new_sets, col, col)
                sets = new_sets


if __name__ == '__main__':
    rows, cols = 10, 10
    maze = MazeEller(rows, cols)
    maze.generate()
    print(maze)
