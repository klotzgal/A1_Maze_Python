# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import QApplication, QGridLayout, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui.form_ui import Ui_View
from ui.maze import MazeWidget


class View(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.text = 'text'
        self.ui = Ui_View()
        self.gridLayout = QGridLayout(self)
        self.ui.setupUi(self)

        maze_widget = MazeWidget(self.ui.left_aside)
        maze_widget.setObjectName('maze_widget')
        maze_widget.setGeometry(QRect(0, 0, 500, 500))
        # self.gridLayout.addWidget(maze_widget)
        # widget = QWidget(self)
        # widget.setStyleSheet('background-color: rgb(0, 255, 0)')
        # self.gridLayout.addWidget(widget)
        # self.gridLayout.addWidget(QWidget(self), 1, 1)
        # self.ui.main_layout.addWidget(maze_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = View()
    widget.show()
    sys.exit(app.exec())
