Summary
-------

Setup is distributed across four services. `airflow` and `postgresql` are part of `apache airflow` ecosystem.

`airflow`: In our case, airflow periodically (Every 10 min) pulls data from currecy exchange site and Push it to InfluxDB.

`postgresql`: Act as a backend for airflow.

`influxdb`: It stores collected data from Airflow in timeseries manner.

`grafana`: It helps us to visulize real time incoming data from `influxdb`.


How to Execute
--------------
1. Clone repo from Git `git clone https://github.com/sqirelT/takeaway.git`

2. cd `takeaway/dags/` and update `api_key` in to d1.py

3. execute `docker-compose up` (Make sure you are connected to internet before you execute second step)

4. Once all containers are up, Login to grafana (default username/password are `admin:admin`), Go to `+` sign left top, click on `Import`. click on `Upload.json` button right side of panel and upload the `dashboard.json` file.
