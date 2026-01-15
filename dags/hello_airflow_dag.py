from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("🎉 Hello from Airflow DAG!")

with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["poc", "hello"],
) as dag:

    t1 = PythonOperator(
        task_id="say_hello",
        python_callable=hello,
    )
