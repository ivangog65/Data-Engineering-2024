from flask import Flask, request, Response

from lesson_02.sales_loader.sales_data_converter import copy_sales_data_to_avro

sales_converter_app = Flask(__name__)


@sales_converter_app.route('/', methods=['POST'])
def convert_sales_to_avro() -> Response:
    request_data = request.get_json()
    copy_sales_data_to_avro(source_dir=request_data['raw_dir'], target_dir=request_data['stg_dir'])
    return Response(status=201)


if __name__ == '__main__':
    sales_converter_app.run(port=8082)
