from flask import Flask, request, Response

from lesson_02.sales_loader.sales_loader import load_sales_data

sales_loader_app = Flask(__name__)


@sales_loader_app.route('/', methods=['POST'])
def load_sales() -> Response:
    request_data = request.get_json()
    load_sales_data(date=request_data['date'], raw_dir=request_data['raw_dir'])
    return Response(status=201)


if __name__ == '__main__':
    sales_loader_app.run(port=8081)
