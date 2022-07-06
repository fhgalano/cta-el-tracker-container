import pandas as pd
from pathlib import Path


c_map = {
    'RED': 'RED',
    'BLUE': 'BLUE',
    'GREEN': 'G',
    'BROWN': 'BRN',
    'PURPLE': 'P',
    'PURPLE EXPRESS': 'Pexp',
    'YELLOW': 'Y',
    'PINK': 'PNK'
}

reference_path = Path(__file__).parent / 'CTA_-_System_Information_-_List_of__L__Stops.csv'

def get_stp_id(quad, color, direction, stop_name):
    # Process Inputs
    color = color_map(color)

    # Filter Mapping
    route_map = pd.read_csv(reference_path)
    route_map = _get_entries_with_stop_name(stop_name, route_map)
    route_map = _get_entries_of_color(color, route_map)
    route_map = _get_entries_with_direction(direction, route_map)

    # Verify Solution
    _check_if_single_solution(route_map)

    return route_map.STOP_ID.values[0]


def color_map(color):
    return c_map[color.upper()]


def _get_entries_with_stop_name(stop_name, route_map):
    return route_map[route_map.STATION_NAME.str.contains(stop_name)]


def _get_entries_of_color(color, route_map):
    return route_map[route_map[color]]


def _get_entries_with_direction(direction, route_map):
    return route_map[route_map.DIRECTION_ID.str.contains(direction)]


def _check_if_single_solution(route_map):
    if route_map.shape[0] != 1:
        raise Exception("No Single Solution for Station ID")
    else:
        pass

