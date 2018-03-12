import json, sys


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_handler:
        json_content = json.load(file_handler)
    return json_content


def create_list_seats_count_bar(file_data):
    list_seats_count = list()
    for atribut in file_data['features']:
        list_seats_count.append(atribut['properties']['Attributes']['SeatsCount'])
    return list_seats_count


def get_biggest_bar(file_data, list_seats_num):
    for atribut in file_data['features']:
        if max(list_seats_num) == int(atribut['properties']['Attributes']['SeatsCount']):
            print(atribut['properties']['Attributes']['Name'], atribut['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(file_data, list_seats_num):
    for atribut in file_data['features']:
        if min(list_seats_num) == int(atribut['properties']['Attributes']['SeatsCount']):
            print(atribut['properties']['Attributes']['Name'], atribut['properties']['Attributes']['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    try:
        #path_to_file = sys.argv[1]
        path_to_file = 'bars.json'
        get_biggest_bar(load_data(path_to_file), create_list_seats_count_bar(load_data(path_to_file)))
        get_smallest_bar(load_data(path_to_file), create_list_seats_count_bar(load_data(path_to_file)))
    except IndexError:
        print('Enter the path to the file.')
    except FileNotFoundError:
        print('No such file.')
