from airflow import DAG
from airflow import operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = (
#    ...
)

dag = DAG('hello_world', default_args=default_args, schedule_interval=timedelta(days=1))

t1 = BashOperator(
    task_id='say_hello',
    bash_command='echo "Hello World from Airflow!"',
    dag=dag,
)