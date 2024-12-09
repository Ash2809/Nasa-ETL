from airflow import DAG
from airflow.providers.http.operators import SimpleHttpOperator
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago
import json

with DAG(
    dag_id = 'NASA_APOD_POSTGRES',
    start_date = days_ago,
    schedule_interval = '@daily',
    catchup = False
) as dag:
    pass
