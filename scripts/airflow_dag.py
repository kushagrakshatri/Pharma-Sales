#airflow_dag.py

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def clean_and_transform():
    os.system('python scripts/data_cleaning_transformation.py')

def load_to_postgresql():
    os.system('python scripts/load_to_postgresql.py')

def detect_anomalies():
    os.system('python scripts/anomaly_detection.py')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG(
    'sales_data_pipeline',
    default_args=default_args,
    description='A simple sales data pipeline',
    schedule_interval='@daily',
)

t1 = PythonOperator(
    task_id='clean_and_transform',
    python_callable=clean_and_transform,
    dag=dag,
)

t2 = PythonOperator(
    task_id='load_to_postgresql',
    python_callable=load_to_postgresql,
    dag=dag,
)

t3 = PythonOperator(
    task_id='detect_anomalies',
    python_callable=detect_anomalies,
    dag=dag,
)

t1 >> t2 >> t3
