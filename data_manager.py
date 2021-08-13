from requests import get
from constantes import iss_url


def api_data(url, parameter=None):
    if parameter is None:
        response = get(url=url)
    else:
        response = get(url=url, params=parameter)
    response.raise_for_status()

    return response.json()


def iss_pos():
    iss = api_data(iss_url)
    iss_lat = float(iss["iss_position"]["latitude"])
    iss_lng = float(iss["iss_position"]["longitude"])

    return iss_lat, iss_lng
