from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    return 'Hello world!'

dag = DAG('hello_world_ady', description='Simple DAG',
          schedule_interval='@daily',
          start_date=datetime(2024, 10, 6),
          catchup=False,
          tags=['ady'] )

task_hello = PythonOperator(
    task_id='print_hello_ady',
    python_callable=print_hello,
    dag=dag
)

task_hello