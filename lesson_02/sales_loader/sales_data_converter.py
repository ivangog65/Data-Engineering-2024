import json
import os

from fastavro import parse_schema
from fastavro.write import writer

from lesson_02.sales_loader.file_utils import recreate_dir


def load_sales_schema() -> str:
    with open('lesson_02/schemas/sales_schema.json') as schema_file:
        return json.load(schema_file)


def copy_sales_data_to_avro(source_dir: str, target_dir: str):
    recreate_dir(target_dir)
    schema = load_sales_schema()
    for json_file_name in os.listdir(source_dir):
        copy_json_to_avro(source_dir, json_file_name, target_dir, schema)


def get_target_file_name(source_json_file_path: str, target_dir: str) -> str:
    filename, file_extension = os.path.splitext(source_json_file_path)
    return os.path.join(target_dir, filename + '.avro')


def copy_json_to_avro(source_dir: str, source_file_name: str, target_dir: str, schema: str):
    with open(get_target_file_name(source_file_name, target_dir), "wb") as target_avro_file:
        with open(os.path.join(source_dir, source_file_name), "r") as source_json_file:
            records = json.load(source_json_file)
            writer(target_avro_file, parse_schema(schema), records)
