import requests

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
