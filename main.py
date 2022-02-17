from typing import Optional

from fastapi import FastAPI
from cta_requests import get_train_eta
from cta_map import get_stp_id

app = FastAPI()


@app.get("/")
def read_root():
    return "The App is Running"


@app.get("/train_eta/{color}/{station_name}/{direction}")
def read_train_eta(color: str, station_name: str, direction: str):
    station_id = get_stp_id(None, color, direction, station_name)
    print(station_id)
    return get_train_eta(station_id)
