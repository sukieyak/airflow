from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def run_chatv3():
    print("POC: chatv3 DAG is running")
    # ยังไม่ต้องทำจริง
    # subprocess.run(["python", "/opt/airflow/dags/chatv3.py"])

with DAG(
    dag_id="poc_chatv3",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["poc", "chat"],
) as dag:

    run = PythonOperator(
        task_id="run_chatv3",
        python_callable=run_chatv3,
    )
