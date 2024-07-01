

class Cell:

    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
        self.walls: dict[str, bool] = {'top': False, 'left': False,
                                       'right': False, 'bottom': False}
        self.visited: bool = False

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Cell):
            return self.x == value.x and self.y == value.y
        return False


class Maze:

    def __init__(self, rows: int, cols: int) -> None:
        self.rows: int = rows
        self.cols: int = cols
        self.field: list[list[Cell]] = [[Cell(row, col) for row in range(rows)]
                                        for col in range(cols)]

    # Метод для дебага. Выводит стенки с заданной стороны
    def print(self, side: str):
        print('______', side, '______')
        for col in range(self.cols):
            for row in range(self.rows):
                if self.field[col][row].walls[side]:
                    print('1', end=' ')
                else:
                    print('0', end=' ')
            print()
        print('___________________')
