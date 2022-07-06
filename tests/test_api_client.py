from pathlib import Path
from dotenv import load_dotenv
from fastapi.testclient import TestClient

from main import app


# Load in env variables
dotenv_path = Path(__file__).parent.parent / 'secrets.env'
load_dotenv(dotenv_path)
client = TestClient(app)


def test_client_heartbeat():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == "The App is Running"


def test_read_train_eta():
    response = client.get(
        "/train_eta/Red/Belmont/S"
    )

    info = response.json()

    assert response.status_code == 200
    assert info['color'] == 'Red'
    assert info['direction'] == 'Service toward 95th or Loop'
    assert info['stop'] == 'Belmont'
    assert type(info['eta']) == float
