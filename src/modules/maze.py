from typing import Optional, Dict
import copy


class Cell:
    def __init__(self, x: int, y: int, walls: Optional[Dict[str, bool]] = None, set_id: int = 0) -> None:
        self.x: int = x
        self.y: int = y
        if walls is None:
            self.walls: Dict[str, bool] = {
                'top': False,
                'left': False,
                'right': False,
                'bottom': False,
            }
        else:
            self.walls = copy.deepcopy(walls)
        self.set_id = set_id  # Идентификатор множества для алгоритма Эллера

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Cell):
            return self.x == value.x and self.y == value.y
        return False

    def __repr__(self) -> str:
        return f'Cell({self.x}, {self.y}, set_id={self.set_id})'


class Maze:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows: int = rows
        self.cols: int = cols
        self.field: list[list[Cell]] = [
            [Cell(row, col) for row in range(rows)] for col in range(cols)
        ]

    def print(self):
        print(self.rows, "rows, x")
        print(self.cols, "cols, y")
        for col in range(self.cols):
            for row in range(self.rows):
                print(self.field[col][row], end=" ")
            print()
        print(self.field)


if __name__ == "__main__":
    m = Maze(rows=2, cols=5)
    m.print()
