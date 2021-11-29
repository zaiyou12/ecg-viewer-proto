import airflow
from airflow import DAG

from data_fetching.operators.validate_data import ValidateData


dag = DAG(
    dag_id="checking_data_dag",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval=None,
)


validation_data = ValidateData(
    task_id='validation_data',
    dag=dag
)