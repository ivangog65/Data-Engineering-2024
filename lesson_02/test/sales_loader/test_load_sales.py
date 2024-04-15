import os
from unittest import mock

from lesson_02.sales_loader.main import app1


@mock.patch('json.dump')
def test_load_sales(json_dump, mock_api):
    os.environ['AUTH_TOKEN'] = '12345'
    date = '2022-01-01'
    raw_dir = "./lesson_02/build/test/output/raw_dir"
    mock_sales_api_response_data = {
        "id": 1,
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }
    mock_api.get(f"https://fake-api-vycpfa6oca-uc.a.run.app/sales?date={date}&page={1}",
                 status_code=200, json=mock_sales_api_response_data)
    mock_api.get(f"https://fake-api-vycpfa6oca-uc.a.run.app/sales?date={date}&page={2}",
                 status_code=404, json={})

    request_body = {
        "date": date,
        "raw_dir": raw_dir
    }

    sales_loader_app = app1
    with sales_loader_app.test_client() as client:
        response = client.post("/", json=request_body)
        assert 201 == response.status_code
        json_dump.assert_called_once_with(mock_sales_api_response_data, mock.ANY)
