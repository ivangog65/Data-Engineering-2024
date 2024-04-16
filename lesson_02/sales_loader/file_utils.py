from pathlib import Path

SALES_FILE_NAME_FORMAT_JSON = 'sales_{date}_{page}.json'


def recreate_dir(directory_full_path: str):
    Path(directory_full_path).mkdir(parents=True, exist_ok=True)
