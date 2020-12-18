#!/bin/bash

# execute this file after you run pip install
USER_HOME=$(echo $HOME)
echo "User Home : $USER_HOME"
export AIRFLOW_HOME=$USER_HOME/airflow 
echo ${AIRFLOW_HOME}

# run airflow  
airflow initdb

# start airflow
airflow webserver -p 8080
airflow schedular

