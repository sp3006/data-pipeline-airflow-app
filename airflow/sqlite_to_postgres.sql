import psycopg
import os
import airflow

CREATE USER airflow;
CREATE DATABASE airflow;
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;
