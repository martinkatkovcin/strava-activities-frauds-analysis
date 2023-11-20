from typing import Tuple

import requests

from src.api_methods import endpoints


def access_activity_data(access_token:str) -> tuple[dict, dict]:
    headers:dict = {'Authorization': f'Authorization: Bearer {access_token}'}
    parameters:dict = {
        "page": 1,
        "per_page": 200
    }
    my_dataset:dict = requests.get(endpoints.activites_endpoint, headers=headers, params=parameters).json()
    return my_dataset, parameters