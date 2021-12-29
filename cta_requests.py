import requests

from cta_api_calls import RequestCTA, Train


def get_train_eta(station_id: str = None):
    cta = RequestCTA()
    cta_req = requests.get(cta.create_request(stop=station_id))
    return Train(cta_req.json()).info()
