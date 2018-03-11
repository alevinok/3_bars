import json, sys


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_handler:
        json_content = json.load(file_handler)
    return json_content


def get_seats_count_bar(file_data):
    lst_seats_count = list()
    for atribute_seatsCount in file_data['features']:
        lst_seats_count.append(atribute_seatsCount['properties']['Attributes']['SeatsCount'])
    return lst_seats_count


def get_biggest_bar(seats):
    return max(seats)


def get_smallest_bar(seats):
    return min(seats)


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    try:
        #path_to_file = sys.argv[1]
        path_to_file = 'bars.json'
        print(get_biggest_bar(get_seats_count_bar(load_data(path_to_file))))
        print(get_smallest_bar(get_seats_count_bar(load_data(path_to_file))))
        #get_biggest_bar(load_data(path_to_file))
    except IndexError:
        print('Enter the path to the file.')
    except FileNotFoundError:
        print('No such file.')
