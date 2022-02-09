from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
import sys


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Большая задача по Maps API')
        self.setGeometry(200, 200, 600, 450)

        self.map_display = QLabel(self)
        self.map_display.move(0, 0)  # размещение карты на окне
        self.map_display.resize(600, 450)  # размеры окна для карты

        self.pixmap = QPixmap('map.png')  # изображение карты
        self.map_display.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    ex.show()
    sys.exit(app.exec())