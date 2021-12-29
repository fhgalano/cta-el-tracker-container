from typing import Optional

from fastapi import FastAPI
from cta_requests import get_train_eta

app = FastAPI()

@app.get("/")
def read_root():
    return "The App is Running"

@app.get("train_eta/{quadrant}/{color}/{station_id}/{direction}")
def read_train_eta(station_id: str)