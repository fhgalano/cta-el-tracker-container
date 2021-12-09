import requests

import config

class RequestCTA:
    def __init__(self):
        self.base_url = config.base_url
        self.func_map = {
            'key': self.give_key,
            'stop': self.give_station,
            'route': self.give_route_code,
            'max_results': self.give_max_results,
            'output_type': self.give_output_type
        }

    def give_key(self):
        return f"key={config.api_key}"

    def give_station(self, station_id='30256'):
        return f"&stpid={station_id}"

    def give_route_code(self, route_code=None):
        if route_code is not None:
            return f"&rt={route_code}"
        else:
            return ''

    def give_max_results(self, max_res=3):
        return f"&max={max_res}"

    def give_output_type(self, out_type='JSON'):
        return f"&outputType={out_type}"

    def create_request(self, key=None, stop=None, route=None, max_results=None, output_type=None):
        d = locals()
        del d['self']
        reqs = [self.base_url]
        for cta_req, value in d.items():
            if value is None:
                reqs.append(self.func_map[cta_req]())
            else:
                reqs.append(self.func_map[cta_req](value))

        return ''.join(reqs)


if __name__ == '__main__':
    a = RequestCTA()
    print(a.create_request())
    # cta = requests.get(a.create_request())
    # print(cta)
