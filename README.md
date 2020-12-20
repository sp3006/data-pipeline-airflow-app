# data-pipelines-airflow-app
    As a part of this project we are demonstrating how to build the data pipelines using apache airflow as engineering 
    orchestration tool airflow-data-pipeline

# Introduction
    A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to 
    their data warehouseETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.
    The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. 
    The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about 
    the songs the users listen to.

# Data Pipelines with Airflow
    A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse 
    ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.They have decided to bring you into 
    the project and expect you to create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and 
    allow easy backfills. They have also noted that the data quality plays a big part when analyses are executed on top the data warehouse 
    and want to run tests against their datasets after the ETL steps have been executed to catch any discrepancies in the datasets.The source 
    data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs 
    that tell about user activity in the application and JSON metadata about the songs the users listen to.

# Project Overview 
    This project will introduce you to the core concepts of Apache Airflow. To complete the project, you will need to create your 
    own custom operators to perform tasks such as staging the data, filling the data warehouse, and running checks on the data as 
    the final step.We have provided you with a project template that takes care of all the imports and provides four empty operators 
    that need to be implemented into functional pieces of a data pipeline. The template also contains a set of tasks that need to be 
    linked to achieve a coherent and sensible data flow within the pipeline.You'll be provided with a helpers class that contains all 
    the SQL transformations. Thus, you won't need to write the ETL yourselves, but you'll need to execute it with your custom operators.
    
# Tools used:
    Install Python3
    Install Docker
    Udacity or Free tier AWS account and Redshift cluster
  ## Clone repository to local machine
     https://github.com/sp3006/data-pipeline-airflow-app.git
     Change directory to local repository
     cd data-pipeline-airflow-app
  ## Create python virtual environment
      python3 -m venv venv             # create virtualenv
      source venv/bin/activate         # activate virtualenv
      pip install -r requirements.txt  # install requirements
      If you are using python older version please use virtualenv command to create the virtual env.

# Airflow Env:
    Our airflow is runing under the local virtual environment 
    https://localhost:8080
# Steps to configure the redshift using Airflow UI
    On the next create connection page, enter the following values:

        Conn Id: Enter redshift.
        Conn Type: Enter Postgres.
        Host: Enter the endpoint of your Redshift cluster, excluding the port at the end. 
              You can find this by selecting your cluster in the Clusters page of the Amazon 
              Redshift console. 
              See where this is located in the screenshot below. 
        # IMPORTANT: Make sure to NOT include the port 
              at the end of the Redshift endpoint string.
        Schema: Enter dev. This is the Redshift database you want to connect to.
        Login: Enter awsuser.
        Password: Enter the password you created when launching your Redshift cluster.
        Port: Enter 5439.
        Once you've entered these values, select Save.

!https://github.com/sp3006/data-pipeline-airflow-app/issues/2#issue-771130402
       


