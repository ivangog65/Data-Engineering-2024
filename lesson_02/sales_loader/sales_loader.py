import json
import os

from lesson_02.sales_loader.file_utils import recreate_dir, SALES_FILE_NAME_FORMAT_JSON
from lesson_02.sales_loader.sales_api_client import get_sales


def write_response_to_file(response_json: dict, raw_dir: str, date: str, page_number: int):
    file_name = SALES_FILE_NAME_FORMAT_JSON.format(date=date, page=page_number)

    file_path = os.path.join(raw_dir, file_name)
    with open(file_path, 'w') as f:
        json.dump(response_json, f)
        f.close()


def load_sales_data(date: str, raw_dir: str):
    recreate_dir(raw_dir)

    page_number = 1
    while True:
        response = get_sales(date, page_number)
        if response.status_code != 200:
            break
        write_response_to_file(response.json(), raw_dir, date, page_number)
        page_number += 1
