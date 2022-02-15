from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap
import sys
from s import picture
from find_place import find_place


class MyMainWindow(QMainWindow):
    def __init__(self):
        self.coord_x, self.coord_y = map(float, input('Введите координаты (формат ввода: x,y): ').split(','))
        self.scale = float(input('Введите масштаб (формат ввода: x), например, 0.02: '))
        picture(self.coord_x, self.coord_y, self.scale)
        self.space = 'map'

        super(MyMainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Большая задача по Maps API')
        self.setGeometry(200, 200, 800, 500)

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
        self.PgDown.move(610, 60)
        self.PgDown.setText('PgDown')

        self.PgDown.clicked.connect(self.less)

        ###
        self.Up = QPushButton(self)
        self.Up.resize(70, 50)
        self.Up.move(610, 120)
        self.Up.setText('Вверх')

        self.Up.clicked.connect(self.up)

        self.Down = QPushButton(self)
        self.Down.resize(70, 50)
        self.Down.move(610, 170)
        self.Down.setText('Вниз')

        self.Down.clicked.connect(self.down)

        self.Right = QPushButton(self)
        self.Right.resize(70, 50)
        self.Right.move(690, 120)
        self.Right.setText('Вправо')

        self.Right.clicked.connect(self.right)

        self.Left = QPushButton(self)
        self.Left.resize(70, 50)
        self.Left.move(690, 170)
        self.Left.setText('Влево')

        self.Left.clicked.connect(self.left)

        ###
        self.Scheme = QPushButton(self)
        self.Scheme.resize(70, 50)
        self.Scheme.move(610, 230)
        self.Scheme.setText('Схема')

        self.Scheme.clicked.connect(self.scheme)

        self.Satellite = QPushButton(self)
        self.Satellite.resize(70, 50)
        self.Satellite.move(610, 280)
        self.Satellite.setText('Спутник')

        self.Satellite.clicked.connect(self.satellite)

        self.Hybrid = QPushButton(self)
        self.Hybrid.resize(70, 50)
        self.Hybrid.move(610, 330)
        self.Hybrid.setText('Гибрид')

        self.Hybrid.clicked.connect(self.hybrid)

        # поиск места
        self.label_find_place = QLineEdit(self)
        self.label_find_place.resize(590, 35)
        self.label_find_place.move(5, 460)

        self.button_find_place = QPushButton(self)
        self.button_find_place.resize(180, 35)
        self.button_find_place.move(610, 460)
        self.button_find_place.setText('Поиск места')

        self.button_find_place.clicked.connect(self.find)

    def new_map(self, value_pt=False):
        picture(self.coord_x, self.coord_y, self.scale, self.space, value_pt=value_pt)
        self.pixmap = QPixmap('map.png')
        self.map_display.setPixmap(self.pixmap)

    def more(self):
        if self.scale < 90:
            self.scale += 0.001
            self.new_map()

    def less(self):
        if self.scale > 0.0011:
            self.scale -= 0.001
            self.new_map()

    def up(self):
        # ll=179,80 max; ll=-179,-80 min
        if self.coord_y < 79:
            self.coord_y += 0.0001
            self.new_map()

    def down(self):
        if self.coord_y > -79:
            self.coord_y -= 0.0001
            self.new_map()

    def right(self):
        if self.coord_x < 179:
            self.coord_x += 0.0001
            self.new_map()

    def left(self):
        if self.coord_x > -179:
            self.coord_x -= 0.0001
            self.new_map()

    def scheme(self):
        self.space = 'map'
        self.new_map()

    def satellite(self):
        self.space = 'sat'
        self.new_map()

    def hybrid(self):
        self.space = 'sat,skl'
        self.new_map()

    def find(self):
        self.place = self.label_find_place.text()
        self.coord_x, self.coord_y = find_place(self.place)
        self.scale = 0.001
        self.new_map(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    ex.show()
    sys.exit(app.exec())