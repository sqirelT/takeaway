# Container installation start from Base Debian Image
FROM debian

MAINTAINER Tejas Gadaria <gadaria.tejas@gmail.com>

# Install necessary Packages
RUN apt-get update && apt-get install -y wget

RUN apt-get install -y postgresql postgresql-contrib

# Note: The official Debian and Ubuntu images automatically ``apt-get clean``
# after each ``apt-get``

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN echo "/etc/init.d/postgresql start && exit 0" > /etc/rc.local

USER postgres

# Create a PostgreSQL USER, PASSWORD and DB
RUN /etc/init.d/postgresql start && \
    psql --command "CREATE USER airflow WITH SUPERUSER PASSWORD 'airflow';" && \
    createdb -O airflow airflow

# Adjust PostgreSQL configuration so that remote connections to the
# database are possible.
RUN echo "host all  all    0.0.0.0/0  trust" >> /etc/postgresql/11/main/pg_hba.conf

RUN echo "listen_addresses='*'" >> /etc/postgresql/11/main/postgresql.conf

# Expose the PostgreSQL port
EXPOSE 5432

# Add VOLUMEs to allow backup of databases
VOLUME  ["/var/lib/postgresql"]

# Set the default command when container starts
CMD ["/usr/lib/postgresql/11/bin/postgres", "-D", "/var/lib/postgresql/11/main/", "-c", "config_file=/etc/postgresql/11/main/postgresql.conf"]
