import os

import requests
from dotenv import load_dotenv
from requests import Response

load_dotenv()

AUTH_TOKEN = os.getenv('AUTH_TOKEN')
SALES_DATA_ENDPOINT = 'https://fake-api-vycpfa6oca-uc.a.run.app/sales'


def get_sales(date: str, page_number: int) -> Response:
    print("Fetching sales data by date {}. Page index {}".format(date, page_number))
    response = requests.get(
        url=SALES_DATA_ENDPOINT,
        params={'date': date, 'page': page_number},
        headers={'Authorization': AUTH_TOKEN},
    )
    print("Response status code:", response.status_code)
    return response
