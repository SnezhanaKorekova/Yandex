import requests

list_pt = []


def picture(coord_x, coord_y, scale, space='map', new_pt=False, del_pt=False):
    if -179 <= coord_x <= 179 and -79 <= coord_y <= 79 and 0 < scale < 90:
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={coord_x},{coord_y}&spn={scale},{scale}&l={space}"
        # удалить метку
        if del_pt:
            while f'{coord_x},{coord_y}' in list_pt:
                list_pt.remove(f'{coord_x},{coord_y}')

        # поставить метку
        if new_pt:
            list_pt.append(f'{coord_x},{coord_y}')
        if len(list_pt) != 0:
            pt = '&pt='
            for i in range(len(list_pt)):
                if i == 0:
                    pt += f'{list_pt[i]},pm2rdm'
                else:
                    pt += f'~{list_pt[i]},pm2rdm'
        else:
            pt = ''
        map_request += pt
        response = requests.get(map_request)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
    else:
        print('ERROR')
        coord_x, coord_y = map(float, input('Введите координаты (формат ввода: x,y): ').split(','))
        scale = float(input('Введите масштаб (формат ввода: x): '))
        picture(coord_x, coord_y, scale)
