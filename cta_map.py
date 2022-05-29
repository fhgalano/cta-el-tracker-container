import pandas as pd

cta_station_data = pd.read_csv('CTA_-_System_Information_-_List_of__L__Stops.csv')


def get_stp_id(quadrant, color, direction, station_name):
    possible_stations = cta_station_data
    possible_stations = get_stations_with_name(possible_stations, station_name)
    possible_stations = get_stations_with_color(possible_stations, color)
    possible_stations = get_stations_in_direction(possible_stations, direction)

    return possible_stations.STOP_ID


def get_stations_with_name(possible_stations, name):
    return possible_stations[possible_stations.STATION_NAME.str.contains(name)]


def get_stations_with_color(possible_stations, color):
    return possible_stations[possible_stations[color.upper()]]


def get_stations_in_direction(possible_stations, direction):
    return possible_stations[possible_stations.DIRECTION_ID.str.contains(direction)]


if __name__ == "__main__":
    id = get_stp_id('we', 'Red', 'S', 'Belmont')

    print('debug')