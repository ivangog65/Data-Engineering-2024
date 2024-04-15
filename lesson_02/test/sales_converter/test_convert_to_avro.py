import os.path

from lesson_02.sales_loader.sales_converter_api import sales_converter_app


def test_convert_to_avro():
    raw_dir = os.path.join(os.getcwd(), "lesson_02/test/sales_converter/input/raw_dir")
    stg_dir = os.path.join(os.getcwd(), "lesson_02/build/test/output/stg_dir")

    request_body = {
        "raw_dir": raw_dir,
        "stg_dir": stg_dir
    }

    with sales_converter_app.test_client() as client:
        response = client.post('/', json=request_body)
        assert 201 == response.status_code
        assert os.listdir(stg_dir) == ['sales_2022-01-01_1.avro']
