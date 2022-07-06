import pytest
from dotenv import load_dotenv
from pathlib import Path
import requests

from cta_api_calls import RequestCTA, Train
from cta_map import get_stp_id


# Load in env variables
dotenv_path = Path(__file__).parent.parent / 'secrets.env'
load_dotenv(dotenv_path)


@pytest.fixture
def cta_request():
    return RequestCTA()


@pytest.fixture
def stop_id():
    return str(get_stp_id('we', 'Red', 'S', 'Belmont'))


@pytest.fixture
def cta_response(cta_request, stop_id):
    return requests.get(cta_request.create_request(stop=stop_id))


def test_create_request_no_inputs(cta_request, stop_id):
    request = cta_request.create_request(stop=stop_id)
    assert request == 'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?' \
                      'key=6a4216fa323a4117931b90c2ccf27284' \
                      '&stpid=30256' \
                      '&max=3' \
                      '&outputType=JSON' # noqa


def test_train(cta_response):
    train = Train(cta_response.json())
    info = train.info()

    assert info['color'] == 'Red'
    assert info['direction'] == 'Service toward 95th or Loop'
    assert info['stop'] == 'Belmont'
    assert type(info['eta']) == float
