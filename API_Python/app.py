import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows

@app.get("/superheroes")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows

@app.get("/consolas")
def get_consolas():
    rows = ["Xbox One", "Xbox 360", "Xbox Series S", "Xbos Series X" "Play Station 4", "Play Station 5", "Nintendo Switch", "Game Cube"]
    return rows
