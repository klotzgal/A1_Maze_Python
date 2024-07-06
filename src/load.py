from maze import Maze


class Loader:

    def __init__(self, maze: Maze = None) -> None:
        self.maze = maze

    def download(self, file: str) -> Maze:
        # Считывание всего файла
        with open(file, 'r') as f:
            l = [list(map(int, line.split())) for line in f]
        # Создание пустого лабиринта
        rows, cols = l[0]
        self.maze = Maze(rows, cols)
        # Заполнение правых и левых стенок из 1 матрицы
        for col in range(cols):
            i = col + 1
            for j in range(rows):
                if l[i][j] == 1:
                    self.maze.field[col][j].walls['right'] = True
                    if j < rows - 1:
                        self.maze.field[col][j + 1].walls['left'] = True
        # Заполнение нижних и верхних стенок из 2 матрицы
        for col in range(cols):
            i = col + cols + 2
            for j in range(rows):
                if l[i][j] == 1:
                    self.maze.field[col][j].walls['bottom'] = True
                    if col < cols - 1:
                        self.maze.field[col + 1][j].walls['top'] = True
        # Заполнение верхней и левой стенки лабиринта
        for row in range(rows):
            self.maze.field[0][row].walls['top'] = True
        for col in range(cols):
            self.maze.field[col][0].walls['left'] = True
        return self.maze

    def upload(self, file: str, maze: Maze) -> None:
        if maze:
            with open(file, 'w') as f:
                f.write(
                    ' '.join(list(map(str, [maze.rows, maze.cols]))) + '\n')
                for row in maze.field:
                    f.write(
                        ' '.join(list(map(str, [int(i.walls['right']) for i in row]))) + '\n')
                f.write('\n')
                for row in maze.field:
                    f.write(
                        ' '.join(list(map(str, [int(i.walls['bottom']) for i in row]))) + '\n')


if __name__ == '__main__':
    l = Loader()
    m = l.download('files/1.txt')
    m.print('right')
    m.print('left')
    m.print('bottom')
    m.print('top')
    l.upload('files/maze.txt', m)
