import threading

from flask import Flask, request, Response

from lesson_02.sales_loader.sales_data_converter import copy_sales_data_to_avro
from lesson_02.sales_loader.sales_loader import load_sales_data

app1 = Flask(__name__)
app2 = Flask(__name__)


@app1.route('/', methods=['POST'])
def load_sales() -> Response:
    request_data = request.get_json()
    load_sales_data(date=request_data['date'], raw_dir=request_data['raw_dir'])
    return Response(status=201)


@app2.route('/', methods=['POST'])
def convert_sales_to_avro() -> Response:
    request_data = request.get_json()
    copy_sales_data_to_avro(source_dir=request_data['raw_dir'], target_dir=request_data['stg_dir'])
    return Response(status=201)


def run_api_client():
    app1.run(port=8081, threaded=True)


def run_files_converter():
    app2.run(port=8082, threaded=True)


if __name__ == '__main__':
    t1 = threading.Thread(target=run_api_client)
    t2 = threading.Thread(target=run_files_converter)
    t1.start()
    t2.start()
