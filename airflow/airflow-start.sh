#!/bin/bash -e

exec airflow initdb &

sleep 5

exec rabbitmq-server &

sleep 5

exec airflow webserver &

sleep 10

exec airflow scheduler &

sleep 10

export C_FORCE_ROOT="true"
exec airflow worker
