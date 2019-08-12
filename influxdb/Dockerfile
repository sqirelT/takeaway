# Container installation start from Base Debian Image
FROM debian

MAINTAINER Tejas Gadaria <gadaria.tejas@gmail.com>

# Install necessary Packages
RUN apt-get update \
    && apt-get install -y wget \
    && apt-get install -y gnupg2

# Note: The official Debian and Ubuntu images automatically ``apt-get clean``
# after each ``apt-get``

RUN wget -qO- https://repos.influxdata.com/influxdb.key | apt-key add -

RUN /bin/bash -c "source /etc/os-release"

# Adding repos, only one of them should be OK based on the version of the system
RUN echo "deb https://repos.influxdata.com/debian stretch stable" | tee /etc/apt/sources.list.d/influxdb.list

RUN echo "deb https://repos.influxdata.com/debian jessie stable" | tee /etc/apt/sources.list.d/influxdb.list

RUN echo "deb https://repos.influxdata.com/debian wheezy stable" | tee /etc/apt/sources.list.d/influxdb.list

RUN apt-get update && apt-get install influxdb

# Copying file
COPY start_influx.sh /start_influx.sh

# Changing permisson
RUN chmod +x start_influx.sh

# Expose Influx port
EXPOSE 8086

# Add VOLUMEs to to backup Databse
VOLUME /var/lib/influxdb

# Execute the script inside container
ENTRYPOINT ["/start_influx.sh"]
