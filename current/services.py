import os

import requests
from dotenv import load_dotenv
from requests.structures import CaseInsensitiveDict

from config.settings import BASE_DIR

dot_env = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dot_env)


def get_currency():
    URL = f"https://api.freecurrencyapi.com/v1/latest"
    headers = CaseInsensitiveDict()
    headers["apikey"] = os.getenv('CUR_API_KEY')
    resp = (requests.get(URL, headers=headers)).json()['data']['RUB']
    print(resp)


