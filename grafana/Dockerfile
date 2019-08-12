# Container installation start from Base Debian Image
FROM debian

MAINTAINER Tejas Gadaria <gadaria.tejas@gmail.com>

# Install necessary Packages
RUN apt-get update \
    && apt-get install -y wget \
    && apt-get install -y software-properties-common \
    && apt-get install -y gnupg2 \
    && apt-get install -y curl gettext-base \
    && apt-get -y install procps

# Note: The official Debian and Ubuntu images automatically ``apt-get clean``
# after each ``apt-get``

RUN add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"

RUN wget -q -O - https://packages.grafana.com/gpg.key | apt-key add -

RUN apt-get update && apt-get install -y grafana

# Copying file and Changing Permission
COPY ./run.sh /run.sh
RUN chmod +x run.sh

# Copying file and Changing Permission
COPY ./start_grafana.sh /start_grafana.sh
RUN chmod +x start_grafana.sh

# Changing work directory and copying dirctory
WORKDIR /datasources
COPY datasources ./datasources

# Expose Grafana port
EXPOSE 3000

# Execute script inside container
ENTRYPOINT ["/start_grafana.sh"]
