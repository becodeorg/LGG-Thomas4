# Airflow

![Airflow](https://airflow.apache.org/images/feature-image.png)

[Apache Airflow](https://airflow.apache.org/) is a pipeline system to manage jobs.
It’s mainly used to create data-pipeline systems.

This is used a lot in the industry because of its ability to structure code execution. You can also find a lot of tools that are based on Airflow, so mastering this tool will help you with others. [Kubeflow](https://www.kubeflow.org/) is a great example of that.

One nice feature of Airflow is that it enables you to easily build scheduled data pipelines using a flexible Python framework.

## Get started

To start with Airflow, I recommend you to go over [this Datacamp course](https://app.datacamp.com/learn/courses/introduction-to-airflow-in-python).

When completed, you should have a clear vision of all the concepts below:

## Key concepts

- DAGS/tasks
- Operators
- Schedule
- Sensors
- Executors
- SLAs
- Branching

<img src="https://static.vecteezy.com/system/resources/previews/006/365/814/original/trendy-key-concepts-vector.jpg" alt="Key concepts" width="200"/>

### DAGs

DAGs are workflow and pipelines. They are a complete pipeline that can perform various tasks that are or are not connected to each other.

### Operators

Operators are tasks. You can define multiple kinds of operators:

- The `BashOperator` executes Bash code.
- The `PythonOperator` executes Python code.

### Schedule

DAGs schedule is a way to schedule DAGs a specific times.

It can be to run a DAG every X time or to define when it should be executed once at a specific time.

### Sensors

Sensors are a way to react to an event in a pipeline.

It can be used to wait for a file to be created before proceeding, or to perform a different task if a Database doesn’t contain what’s expected,…

### Executors

Executors are how Airflow is gonna be executed. It will define where the code is gonna be executed.

You can define which executor should be used in the Airflow configuration file.

Some executors:

- `SequentialExecutor`: The default, will execute tasks 1 at a time. Useful for debugging but **should NOT be used in production.**
- `LocalExecutor`: Run on a single system, let you define how it should be parallelized, and can use the resources of the host.
- `CeleryExecuter`: More the “cluster” way. Let you set up multiple workers and hosts. More complex to set up but more flexible and powerful.

### Configuration

#### DAG folder

You can define where Airflow should look for the DAGs file. It’s under the variable `dags_folder`. **Note that the path NEEDS to be ABSOLUTE!**

### Debug

If you have errors in your DAGs, you can print them with: `airflow list_dags` CLI.

### SLA

SLA stands for **Service Level Agreement.** 

If a task/DAG can’t meet the timing requirements, it will trigger an **SLA Miss** which will send an email (configured in the Airflow config) and show an error in the logs. 

### Templates

When you define your tasks, you can use templates to define template commands:

```python
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
  'start_date': datetime(2020, 4, 15),
}

cleandata_dag = DAG('cleandata',
                    default_args=default_args,
                    schedule_interval='@daily')

templated_command = """
  bash cleandata.sh {{ params.filename }}
"""

clean_task = BashOperator(task_id='cleandata_task',
                          bash_command=templated_command,
                          params={'filename': "data.csv"},
                          dag=cleandata_dag)

clean_task2 = BashOperator(task_id='cleandata_task2',
                          bash_command=templated_command,
                          params={'filename': "report.csv"},
                          dag=cleandata_dag)
                           
# Set the operator dependencies
clean_task >> clean_task2 
```

### Branching

In Airflow, Branching lets you use conditional logic in your pipelines.

Example:

```python
def check_odd_days(**kwargs):
    if int(kwargs['ds_nodash'] % 2 == 0):
        return "even_day_task"
    else:
        return "odd_day_task"

branch_task = BranchPythonOperator(
    task_id="odd_day_checking",
    dag=dag,
    provide_content=True,
    python_callable=check_odd_days
)

# In case it's odd
branch_task >> odd_day_task
branch_task >> even_day_task
```

Now that you are familiar with the key concepts, let's apply your knowledge to a real scenario!

## Additional resources
- [Awesome Apache Airflow](https://github.com/jghoman/awesome-apache-airflow) - A curated list of resources
- [ETL best practices with Airflow](https://gtoonstra.github.io/etl-with-airflow/) 
