import requests


def picture(coord_x, coord_y, scale, space='map', value_pt=False):
    if -179 <= coord_x <= 179 and -79 <= coord_y <= 79 and 0 < scale < 90:
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={coord_x},{coord_y}&spn={scale},{scale}&l={space}"
        if value_pt:  # поставить метку
            map_request += f'&pt={coord_x},{coord_y},pm2rdm'
        response = requests.get(map_request)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
    else:
        print('ERROR')
        coord_x, coord_y = map(float, input('Введите координаты (формат ввода: x,y): ').split(','))
        scale = float(input('Введите масштаб (формат ввода: x): '))
        picture(coord_x, coord_y, scale)
