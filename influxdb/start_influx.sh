#!/bin/bash -e

exec influxd &

sleep 2

until wget -q "http://localhost:8086/ping" 2> /dev/null; do
    sleep 1
done

influx -host=localhost -port=8086 -execute="CREATE USER ${INFLUX_USER} WITH PASSWORD '${INFLUX_PASSWORD}' WITH ALL PRIVILEGES"
influx -host=localhost -port=8086 -execute="CREATE DATABASE ${INFLUX_DB}"

kill -s TERM %1

sleep 5

exec influxd
