#!/bin/bash -e

exec /run.sh &

sleep 2

curl -s -X POST -H "Content-Type: application/json" -d @datasources/influx.json \
"http://localhost:3000/api/datasources" -u $GF_USER:$GF_PASSWORD

sleep 2

kill $(pgrep grafana)

sleep 5

exec /run.sh
