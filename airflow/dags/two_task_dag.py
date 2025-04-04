'''Two Task DAG'''
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG

# Define default arguments for the DAG
default_args = {
    'owner': 'Vinoo',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'catchup': False,
    'start_date': datetime(2023, 1, 1)
}

# Define the DAG
with DAG(
    dag_id='two_task_dag',  # Corrected the DAG ID to match the purpose
    description='A two task Airflow DAG',  # Added missing comma here
    schedule_interval=None,
    default_args=default_args
) as dag:

    # Define the first task
    t0 = BashOperator(
        task_id='bash_task_0',
        bash_command='echo "First Airflow task!"'
    )

    # Define the second task
    t1 = BashOperator(
        task_id='bash_task_1',
        bash_command='echo "Sleeping..." && sleep 5s && echo "Second Airflow task!"'
    )

    # Set task dependencies
    t0 >> t1
