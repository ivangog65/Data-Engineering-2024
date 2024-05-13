import os
from datetime import datetime
from typing import Any

import requests
from airflow import DAG
from airflow.models import Param
from airflow.operators.python import PythonOperator

JOB1_PORT = 8081
JOB2_PORT = 8082


def extract_data(**task_context) -> Any:
    print("Starting job1:")

    date = task_context.get("ds")
    raw_dir = task_context.get("params")["raw_dir"]
    resp = requests.post(
        url=f'http://localhost:{JOB1_PORT}/',
        json={
            "date": date,
            "raw_dir": os.path.join(raw_dir, date)
        }
    )
    assert resp.status_code == 201


def convert_data(**task_context) -> Any:
    print("Starting job2:")

    date = task_context.get("ds")
    raw_dir = task_context.get("params")["raw_dir"]
    stg_dir = task_context.get("params")["stg_dir"]
    resp = requests.post(
        url=f'http://localhost:{JOB2_PORT}/',
        json={
            "raw_dir": os.path.join(raw_dir, date),
            "stg_dir": os.path.join(stg_dir, date)
        }
    )
    assert resp.status_code == 201


with DAG(
        dag_id='process_sales',
        schedule="0 1 * * *",
        params={
            "raw_dir": Param(
                default='/Users/artur/PycharmProjects/Data-Engineering-2024/lesson_07/test_data/raw/sales/'),
            "stg_dir": Param(
                default='/Users/artur/PycharmProjects/Data-Engineering-2024/lesson_07/test_data/stg/sales/')
        },
        start_date=datetime(2022, 8, 9),
        end_date=datetime(2022, 8, 12),
        catchup=True,
        max_active_runs=1,
        tags=['lesson_07']
) as dag:
    extract_task = PythonOperator(
        task_id='extract_data_from_api',
        python_callable=extract_data
    )

    transform_task = PythonOperator(
        task_id='convert_to_avro',
        python_callable=convert_data
    )
    extract_task >> transform_task
