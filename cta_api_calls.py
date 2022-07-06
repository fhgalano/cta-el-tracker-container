import datetime
import requests

import os
from dotenv import load_dotenv

load_dotenv('secrets.env')


class RequestCTA:
    def __init__(self):
        self.base_url = os.getenv('BASE_URL')
        self.func_map = {
            'key': self.give_key,
            'stop': self.give_station,
            'route': self.give_route_code,
            'max_results': self.give_max_results,
            'output_type': self.give_output_type
        }

    @staticmethod
    def give_key():
        return f"key={os.getenv('API_KEY')}"

    @staticmethod
    def give_station(station_id='30256'):
        return f"&stpid={station_id}"

    @staticmethod
    def give_route_code(route_code=None):
        if route_code is not None:
            return f"&rt={route_code}"
        else:
            return ''

    @staticmethod
    def give_max_results(max_res=3):
        return f"&max={max_res}"

    @staticmethod
    def give_output_type(out_type='JSON'):
        return f"&outputType={out_type}"

    def create_request(self,
                       key=None,
                       stop=None,
                       route=None,
                       max_results=None,
                       output_type=None):
        d = {'key': key,
             'stop': stop,
             'route': route,
             'max_results': max_results,
             'output_type': output_type}
        reqs = [self.base_url]
        for cta_req, value in d.items():
            if value is None:
                reqs.append(self.func_map[cta_req]())
            else:
                reqs.append(self.func_map[cta_req](value))

        return ''.join(reqs)


class Train:
    def __init__(self, cta_response):
        self.eta = cta_response['ctatt']['eta']
        self.time = cta_response['ctatt']['tmst']

        # Parse eta data
        self.dly = self.is_delayed()
        self.color = self.route_color()
        self.stop = self.current_stop()
        self.direction = self.route_direction()
        self.eta = self.eta_calc()

    def is_delayed(self):
        return self.eta[0]['isDly']

    def route_color(self):
        return self.eta[0]['rt']

    def current_stop(self):
        return self.eta[0]['staNm']

    def route_direction(self):
        return self.eta[0]['stpDe']

    def eta_calc(self):
        t0 = (datetime.datetime.strptime(self.eta[0]['prdt']
                                         .replace('T', ' '),
                                         '%Y-%m-%d %H:%M:%S'))
        t1 = (datetime.datetime.strptime(self.eta[0]['arrT']
                                         .replace('T', ' '),
                                         '%Y-%m-%d %H:%M:%S'))

        time_delta = (t1 - t0)
        total_seconds = time_delta.total_seconds()
        return total_seconds/60

    def info(self):
        return {
            'color': self.color,
            'direction': self.direction,
            'stop': self.stop,
            'eta': self.eta
        }


if __name__ == '__main__':
    a = RequestCTA()
    cta = requests.get(a.create_request())
    train = Train(cta.json())
