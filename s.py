import requests


def picture(coord_x, coord_y, scale):
    '''coord_x, coord_y = map(float, input('Введите координаты (формат ввода: x,y): ').split(','))
    scale_x, scale_y = map(float, input('Введите масштаб (формат ввода: x,y): ').split(','))'''

    map_request = f"http://static-maps.yandex.ru/1.x/?ll={coord_x},{coord_y}&spn={scale},{scale}&l=map"
    response = requests.get(map_request)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
