#!/usr/bin/python3
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
### Tutorial Documentation
Documentation that goes along with the Airflow tutorial located
[here](https://airflow.apache.org/tutorial.html)
"""
# [START tutorial]
# [START import_module]
from datetime import timedelta
from logging import getLogger, DEBUG

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# [END import_module]

# this still did not give me the log from bashOperator
# [START default_args]
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
# [END default_args]
print("hellow from tootorial")

# [START instantiate_dag]
dag = DAG(
    'tootorial',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval='@once',
    start_date=days_ago(2),
    tags=['example'],
)
# [END instantiate_dag]

# t1, t2 and t3 are examples of tasks created by instantiating operators
# [START basic_task]
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
    do_xcom_push=True
)

t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)
# [END basic_task]

# [START documentation]
dag.doc_md = __doc__

t1.doc_md = """\
#### Task Documentation
You can document your task using the attributes `doc_md` (markdown),
`doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
rendered in the UI's Task Instance Details page.
![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
"""
# [END documentation]



# [START jinja_template]
templated_command = """
{% for i in range(5) %}
    echo "{{ ds }}"
    echo "{{ macros.ds_add(ds, 7)}}"
    echo "{{ params.my_param }}"
{% endfor %}
"""

t3 = BashOperator(
    task_id='templated',
    depends_on_past=False,
    bash_command=templated_command,
    params={'my_param': f'Parameter I passed in'},
    # params={'my_param': f'Parameter I passed in:{os.getpid()}'},
    dag=dag,
    do_xcom_push=True
)
# [END jinja_template]

# This means that t2 will depend on t1
# running successfully to run.
# t1.set_downstream(t2)
# The bit shift operator can also be
# used to chain operations:
# t1 >> t2

# Chaining multiple dependencies becomes
# concise with the bit shift operator:
# t1 >> t2 >> t3

# A list of tasks can also be set as
# dependencies. These operations
# all have the same effect:
# t1.set_downstream([t2, t3])
t1 >> [t2, t3]
# [t2, t3] << t1
#t2 >> t1 >> t2 >> t3
print("blah2")


# [END tutorial]