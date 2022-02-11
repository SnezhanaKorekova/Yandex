from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
import sys
import requests


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
    # coord_x, coord_y = map(float, input('Введите координаты (формат ввода: x y): ').split())
    # scale_x, scale_y = map(float, input('Введите масштаб (формат ввода: x y): ').split())
    coord_x, coord_y = 37.677751, 55.757718
    scale_x, scale_y = 0.016457,0.00619

    map_request = f"http://static-maps.yandex.ru/1.x/?ll={coord_x},{coord_y}&spn={scale_x},{scale_y}&l=map"
    response = requests.get(map_request)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    app = QApplication(sys.argv)
    ex = MyMainWindow()
    ex.show()
    sys.exit(app.exec())