import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id="test_dag",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval=None,
)



def print_conf(**context):
    print(context["dag_run"].conf)

process = PythonOperator(
 task_id="process",
 python_callable=print_conf,
 dag=dag,
)