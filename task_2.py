from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QPixmap
import sys
from s import picture


class MyMainWindow(QMainWindow):
    def __init__(self):
        # self.coord_x, self.coord_y = map(float, input('Введите координаты (формат ввода: x,y): ').split(','))
        # self.scale = float(input('Введите масштаб (формат ввода: x): '))
        self.coord_x, self.coord_y = 37.677751, 55.757718
        self.scale = 1.5
        picture(self.coord_x, self.coord_y, self.scale)

        super(MyMainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Большая задача по Maps API')
        self.setGeometry(200, 200, 800, 450)

        self.map_display = QLabel(self)
        self.map_display.move(0, 0)  # размещение карты на окне
        self.map_display.resize(600, 450)  # размеры окна для карты

        self.pixmap = QPixmap('map.png')  # изображение карты
        self.map_display.setPixmap(self.pixmap)

        ##
        self.PgUp = QPushButton(self)
        self.PgUp.resize(70, 50)
        self.PgUp.move(610, 10)
        self.PgUp.setText('PgUp')

        self.PgUp.clicked.connect(self.more)

        self.PgDown = QPushButton(self)
        self.PgDown.resize(70, 50)
        self.PgDown.move(610, 70)
        self.PgDown.setText('PgDown')

        self.PgDown.clicked.connect(self.less)

    def more(self):
        if self.scale < 20:
            self.scale += 0.5
        print(self.scale)
        picture(self.coord_x, self.coord_y, self.scale)
        self.pixmap = QPixmap('map.png')
        self.map_display.setPixmap(self.pixmap)

    def less(self):
        if self.scale > 0.6:
            self.scale -= 0.5
        print(self.scale)
        picture(self.coord_x, self.coord_y, self.scale)
        self.pixmap = QPixmap('map.png')
        self.map_display.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    ex.show()
    sys.exit(app.exec())