# Container installation start from Base Debian Image
FROM debian

MAINTAINER Tejas Gadaria <gadaria.tejas@gmail.com>

# Setting up envrionment variable for build and runtime.
ENV AIRFLOW_HOME=/root/airflow
ENV AIRFLOW_GPL_UNIDECODE=yes

# Install necessary Packages
RUN apt-get -y update \
    && apt-get install -y python-setuptools \
    && apt-get install -y python-pip \
    && pip install --upgrade pip \
    && apt install -y libpq-dev python-dev \
    && apt-get install -y libssl-dev \
    && apt-get install -y libkrb5-dev \
    && apt-get install -y libsasl2-dev \
    && pip install apache-airflow[celery,crypto,rabbitmq]

# Install necessary Packages
RUN apt-get install -y rabbitmq-server \
    && pip install psycopg2 \
    && pip install influxdb

# Note: The official Debian and Ubuntu images automatically ``apt-get clean``
# after each ``apt-get``

# Updating Rabbimq configuration
RUN echo "NODE_IP_ADDRESS=0.0.0.0" >> /etc/rabbitmq/rabbitmq-env.conf

# Copy airflow configuration file
COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

# Copying file and Changing Permission
COPY airflow-start.sh /airflow-start.sh
RUN chmod +x airflow-start.sh

# Expose port for Airflow webserver, RabitmQ and log server
EXPOSE 8080 5672 8793

# Execute script inside container
ENTRYPOINT ["/airflow-start.sh"]
