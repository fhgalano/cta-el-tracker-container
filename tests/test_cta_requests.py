from dotenv import load_dotenv
from pathlib import Path

from cta_requests import get_train_eta

# Load in env variables
dotenv_path = Path(__file__).parent.parent / 'secrets.env'
load_dotenv(dotenv_path)


def test_train_eta():
    info = get_train_eta()

    assert info['color'] == 'Red'
    assert info['direction'] == 'Service toward 95th or Loop'
    assert info['stop'] == 'Belmont'
    assert type(info['eta']) == float
