import json, sys
from math import sqrt, pow


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_handler:
        json_content = json.load(file_handler)
    return json_content


def create_list_seats_count_bar(file_data):
    seats_count = list()
    for atribut in file_data['features']:
        seats_count.append(atribut['properties']['Attributes']['SeatsCount'])
    return seats_count


def create_dict_bars_coordinates(file_data):
    bars_coordinates = dict()
    for atribut in file_data['features']:
        bars_coordinates[atribut['properties']['Attributes']['Name']] = \
            atribut['geometry']['coordinates']
    return bars_coordinates


def get_biggest_bar(file_data, list_seats):
    big_bars = dict()
    for atribut in file_data['features']:
        if max(list_seats) == \
                int(atribut['properties']['Attributes']['SeatsCount']):
            big_bars[atribut['properties']['Attributes']['Name']] \
                = atribut['properties']['Attributes']['SeatsCount']
    return big_bars.items()


def get_smallest_bar(file_data, list_seats):
    small_bars = dict()
    for atribut in file_data['features']:
        if min(list_seats) == \
                int(atribut['properties']['Attributes']['SeatsCount']):
            small_bars[atribut['properties']['Attributes']['Name']] \
                    = atribut['properties']['Attributes']['SeatsCount']
    return small_bars.items()


def euclidean_distance(longitude, latitude, user_longitude, user_latitude):
    distance = sqrt(pow((float(longitude) - float(user_longitude)), 2) + \
                    pow((float(latitude) - float(user_latitude)), 2))
    return distance


def get_closest_bar(coordinate_data, user_longitude, user_latitude):
    closest_bars_dict = dict()
    distance = list()
    for key, value in coordinate_data.items():
        closest_bars_dict[key] = \
            euclidean_distance(value[0], value[1], user_longitude, user_latitude)
    for dist in closest_bars_dict.values():
        distance.append(dist)
    for name_bar, dist_bar in closest_bars_dict.items():
        if min(distance) == dist_bar:
            print('\t%s.' % name_bar)


if __name__ == '__main__':
    try:
        #path_to_file = sys.argv[1]
        path_to_file = 'bars.json'
        received_file = load_data(path_to_file)
        seats_bars = create_list_seats_count_bar(received_file)

        print('\nСамый большой бар: ')
        for key, value in get_biggest_bar(received_file, seats_bars):
            print('\t%s: %s мест.' % (key, value))

        print('\nСамый маленький бар: ')
        for key, value in get_smallest_bar(received_file, seats_bars):
            print('\t%s: %s мест.' % (key, value))

        print('\nВведите Ваши координаты: ')
        user_longitude = input('долгота: ')
        user_latitude = input('широта: ')
        try:
            float(user_longitude)
            float(user_latitude)
            print('\nБлижайший бар: ')
            coordinate_bars_dict = create_dict_bars_coordinates(load_data(path_to_file))
            get_closest_bar(coordinate_bars_dict, user_longitude, user_latitude)
        except ValueError:
            print('\nВведён неверный формат координат.\n')

    except IndexError:
        print('Enter the path to the file.')
    except FileNotFoundError:
        print('No such file.')
