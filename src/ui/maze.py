import random

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QPainter, QPaintEvent, QPen
from PySide6.QtWidgets import QWidget

from modules.algorithm import bfs, get_path
from modules.load import Loader
from modules.maze import Cell, Maze


class MazeWidget(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent, Qt.WindowType.Widget)
        file = 'tests/files/3.txt'
        self.text = file
        try:
            self.maze: Maze = Loader().download(file)
            self.STEP: int = 500 / max(self.maze.cols, self.maze.rows)
            frm: list[list[tuple[int, int]]] = bfs(self.maze, (2, 3))
            self.path: list[tuple[int, int]] = get_path(frm, (16, 10))
        except Exception as e:
            print(e)

    def paintEvent(self, event: QPaintEvent) -> None:
        qp = QPainter()
        qp.begin(self)
        # self.drawText(event, qp)
        # self.drawPoints(qp)
        self._draw_maze(qp)
        qp.end()
        return super().paintEvent(event)

    def drawText(self, event, qp):
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)

    def _draw_maze(self, qp) -> None:
        if self.maze is None:
            return

        pen = QPen(Qt.red, 2, Qt.SolidLine)

        qp.setPen(pen)
        for y in range(self.maze.cols):
            for x in range(self.maze.rows):
                cell: Cell = self.maze.field[y][x]
                if cell.walls['top']:
                    qp.drawLine(
                        x * self.STEP, y * self.STEP, (x + 1) * self.STEP, y * self.STEP
                    )
                if cell.walls['bottom']:
                    qp.drawLine(
                        x * self.STEP,
                        (y + 1) * self.STEP,
                        (x + 1) * self.STEP,
                        (y + 1) * self.STEP,
                    )
                if cell.walls['right']:
                    qp.drawLine(
                        (x + 1) * self.STEP,
                        y * self.STEP,
                        (x + 1) * self.STEP,
                        (y + 1) * self.STEP,
                    )
                if cell.walls['left']:
                    qp.drawLine(
                        x * self.STEP, y * self.STEP, x * self.STEP, (y + 1) * self.STEP
                    )
