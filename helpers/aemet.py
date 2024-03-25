import requests

from helpers.database import queries
from helpers.database.sqlite import Database
from settings import AEMET_API_KEY


class AemetConnectionError(Exception):
    pass


class AemetConnection:
    """
    Class to connect to Aemet API
    """
    HEADERS: dict[str, str] = {'cache-control': "no-cache"}
    PARAMS: dict[str, str] = {"api_key": AEMET_API_KEY}
    GET_TOWNS_URL = "https://opendata.aemet.es/opendata/api/maestro/municipios"

    def get_towns(self) -> list[dict[str, str]]:
        response = requests.get(self.GET_TOWNS_URL, headers=self.HEADERS, params=self.PARAMS)
        if response.status_code == 200:
            return response.json()
        raise AemetConnectionError("AEMET connection error when try to get towns")

    def insert_towns(self, towns: list[dict[str, str]]):
        database = Database()
        database.execute(queries.CREATE_TOWNS_TABLE)
        for town in towns:
            town_id = town["id"]
            town_name = town["nombre"]
            database.execute(queries.INSERT_TOWN, (town_id, town_name))
