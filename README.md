## Why Airflow
Among python [workflow frameworks on Github](https://github.com/pditommaso/awesome-pipeline):
* Airflow > 7,000 forks
* Luigi and Ray > 2,000 forks
* others < 1000

Third party [integrations](https://airflow.apache.org/docs/)

Supported  [backends](https://airflow.apache.org/docs/apache-airflow/stable/executor/index.html)



## Airflow tutorial

The Airflow [tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.) seems 
to be outdated. Here is aversion that might work for the next couple of days. In particular, 
you may find yourself working through the section called Tutorial, only to discover that this way of 
doing things was obsoleted in Airflow 2.0.

If you don't like junk in your home dir

`export AIRFLOW_HOME="/some/reasonable/place"`

Keep in mind that sypu might want to run the scheduler or the webserver from another instance og the shell,
 so you might want to place this in bashrc.


`sudo pip3 install apache-airflow`

`airflow db init`

Note you do not need to instantiate the user, run schedule, nor run the webserver to run the scripts provided in the
tutorial/

Stumbled me for a while: your dags _must_ be in a directory defined in airflow.cfg 
called dags_folder.

Not sure what is the purpose of running your dag script from python, as suggested by tutorial.
Instead, if your python compile, you should be able to see the name of your dag is you do

`airflow dags list`
If you don's see it, it either does not compile, or it is not on the path where airflow expects it.

Testing each task separately

`airflow tasks test tootorial  print_date 2015-06-01`

Running the whole dag:
`airflow dags trigger tootorial`

The loogin is completely messed up, so you cannnot see the stdout from BashOPerator anywhere.
In a bizzare remedy, the webserver will show you, linked from each instance of the task that ran,  what _would_ the
templated command lok like, if [had you ran it](https://marclamberti.com/blog/airflow-bashoperator/) 
(but you did, because this option is linked from the log [?!])