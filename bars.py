import json, sys
from math import sqrt, pow


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_handler:
        json_content = json.load(file_handler)
    return json_content


def create_list_seats_count_bar(file_data):
    list_seats_count = list()
    for atribut in file_data['features']:
        list_seats_count.append(atribut['properties']['Attributes']['SeatsCount'])
    return list_seats_count


def create_dict_bars_coordinates(file_data):
    bars_coordinates_dict = dict()
    for atribut in file_data['features']:
        bars_coordinates_dict[atribut['properties']['Attributes']['Name']] \
            = atribut['geometry']['coordinates']
    return bars_coordinates_dict


def get_biggest_bar(file_data, list_seats):
    big_bars_dict = dict()
    for atribut in file_data['features']:
        if max(list_seats) == int(atribut['properties']['Attributes']['SeatsCount']):
            big_bars_dict[atribut['properties']['Attributes']['Name']] \
                = atribut['properties']['Attributes']['SeatsCount']
    return big_bars_dict


def get_smallest_bar(file_data, list_seats):
    small_bars_dict = dict()
    for atribut in file_data['features']:
        if min(list_seats) == int(atribut['properties']['Attributes']['SeatsCount']):
            small_bars_dict[atribut['properties']['Attributes']['Name']] \
                    = atribut['properties']['Attributes']['SeatsCount']
    return small_bars_dict


def printing_dict_basr(dict_bars):
    for key, value in dict_bars.items():
        print('\t', chr(183), '%s: %s мест.' % (key, value))


def printing_closest_basr(name_bar):
    print('\t', chr(183), '%s.' % name_bar)


def euclidean_distance(longitude, latitude, user_longitude, user_latitude):
    try:
        distance = sqrt(pow((float(longitude) - float(user_longitude)), 2) + \
                        pow((float(latitude) - float(user_longitude)), 2))
        return distance
    except ValueError:
        print('Введены неверные координаты.')
        exit(0)


def get_closest_bar(coordinate_data, user_longitude, user_latitude):
    closest_bars_dict = dict()
    distance = list()
    for key, value in coordinate_data.items():
        closest_bars_dict[key] = euclidean_distance(value[0], value[1], user_longitude, user_latitude)
    for dist in closest_bars_dict.values():
        distance.append(dist)
    for name_bar, dist_bar in closest_bars_dict.items():
        if min(distance) == dist_bar:
            print('\t', chr(183), '%s.' % name_bar)


if __name__ == '__main__':
    try:
        path_to_file = sys.argv[1]
        #path_to_file = 'bars.json'
        received_file = load_data(path_to_file)
        list_seats_bars = create_list_seats_count_bar(load_data(path_to_file))
        print('\nСамый большой бар: ')
        printing_dict_basr(get_biggest_bar(received_file, list_seats_bars))
        print('\nСамый маленький бар: ')
        printing_dict_basr(get_smallest_bar(received_file, list_seats_bars))
        print('\nВведите Ваши координаты: ')
        user_longitude = input('долгота: ')
        user_latitude = input('широта: ')
        coordinate_bars_dict = create_dict_bars_coordinates(load_data(path_to_file))
        print('\nБлижайший бар: ')
        get_closest_bar(coordinate_bars_dict, user_longitude, user_latitude)
    except IndexError:
        print('Enter the path to the file.')
    except FileNotFoundError:
        print('No such file.')
