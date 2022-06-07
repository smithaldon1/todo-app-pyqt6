import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.Qt import *
from PySide6.QtGui import *

class MainWindow(QMainWindow):
    """
    Class definition for the main window
    @function: __init__(self) --> window initialization
    @function: 
    """
    def __init__(self):
        super().__init__()

        # Window Properties
        self.setWindowTitle("Todo App | PySide6")
        self.setMinimumSize(QSize(800, 600))

        l = QLabel("Main Window")
        l.setMargin(10)
        self.setCentralWidget(l)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec()