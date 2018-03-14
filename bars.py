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
    print()


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    try:
        #path_to_file = sys.argv[1]
        path_to_file = 'bars.json'
        parsed_file = load_data(path_to_file)
        list_seats_bars = create_list_seats_count_bar(load_data(path_to_file))
        #printing_dict_basr(get_biggest_bar(parsed_file, list_seats_bars))
        print('Самый большой бар: ')
        printing_dict_basr(get_biggest_bar(parsed_file, list_seats_bars))
        print('Самый маленький бар: ')
        printing_dict_basr(get_smallest_bar(parsed_file, list_seats_bars))
    except IndexError:
        print('Enter the path to the file.')
    except FileNotFoundError:
        print('No such file.')
