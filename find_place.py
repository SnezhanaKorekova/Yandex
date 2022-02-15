import requests


def find_place(toponim_to_find):
    toponim_to_find = '+'.join(toponim_to_find.split())

    server_gtocoder = 'http://geocode-maps.yandex.ru/1.x/'
    params = {'apikey': "40d1649f-0493-4b70-98ba-98533de7710b",
              'geocode': toponim_to_find,
              'format': 'json'}

    response_geocoder = requests.get(server_gtocoder, params=params)
    json_response = response_geocoder.json()

    pos = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    coord_x, coord_y = pos.split()

    full_address = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']

    return float(coord_x), float(coord_y), full_address
