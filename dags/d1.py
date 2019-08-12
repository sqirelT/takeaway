from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from influxdb import InfluxDBClient
import requests

url = 'https://www.alphavantage.co/query?'
api_key = '<YOUR API KEY>'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': True,
    'email': ['gflabs01@gmail.com'],
    'start_date': datetime(2019, 8, 9),
    'retries': 0
}

dag = DAG('dag1', default_args=default_args, schedule_interval=timedelta(seconds=600))


def get_data(function, from_currency, to_currency):
    payload = {"function": function, "from_currency": from_currency,
               "to_currency": to_currency, "apikey": api_key}
    resp = requests.get(url, params=payload).json()

    series = []
    table_points = {
        "time": resp['Realtime Currency Exchange Rate']['6. Last Refreshed'],
        "measurement": "currency_exchange_rate",
        "fields": {
            "exchange_rate": resp['Realtime Currency Exchange Rate']['5. Exchange Rate'],
        },
        "tags": {
            "from_currency": resp['Realtime Currency Exchange Rate']['2. From_Currency Name'],
            "to_currency": resp['Realtime Currency Exchange Rate']['4. To_Currency Name']
        },
    }
    series.append(table_points)
    return series


def to_influxdb(host, user, password, dbname, **kwargs):
    ti = kwargs['ti']
    client = InfluxDBClient(host=host, port=8086, username=user, password=password, database=dbname)
    client.create_database(dbname)
    client.switch_database('exchange')
    retention_policy = 'server_data'
    client.create_retention_policy(retention_policy, '3d', 3, default=True)
    data = ti.xcom_pull(task_ids='pull_data')
    client.write_points(data, retention_policy=retention_policy)


pull_data = PythonOperator(
    task_id='pull_data',
    python_callable=get_data,
    op_args=["CURRENCY_EXCHANGE_RATE", "BTC", "USD"],
    dag=dag
)


push_to_influx = PythonOperator(
    task_id='push_to_influx',
    python_callable=to_influxdb,
    op_args=['influxdb', 'root', 'redhat', 'exchange'],
    provide_context=True,
    dag=dag
)

pull_data >> push_to_influx
