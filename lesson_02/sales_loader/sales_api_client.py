import os

import requests
from dotenv import load_dotenv
from requests import Response

load_dotenv()

AUTH_TOKEN = os.getenv('AUTH_TOKEN')


def get_sales(date: str, page_number: int) -> Response:
    print("Fetching sales data by date {}. Page index {}".format(date, page_number))
    response = requests.get(
        url='https://fake-api-vycpfa6oca-uc.a.run.app/sales',
        params={'date': date, 'page': page_number},
        headers={'Authorization': AUTH_TOKEN},
    )
    print("Response status code:", response.status_code)
    return response
