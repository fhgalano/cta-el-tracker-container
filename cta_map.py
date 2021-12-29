import pandas as pd

map = pd.read_csv('CTA_-_System_Information_-_List_of__L__Stops.csv')

def get_stp_id(quad, color, direction, stop_name):

    sf = map[map.STATION_NAME.str.contains(stop_name)]
    sf = sf[sf[color.upper()]]
    sf = sf[sf.DIRECTION_ID.str.contains(direction)]

    return sf.STOP_ID


if __name__ == "__main__":
    id = get_stp_id('we', 'Red', 'S', 'Belmont')

    print('debug')