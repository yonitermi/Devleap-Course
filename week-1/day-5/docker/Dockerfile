FROM ubuntu:18.04

# Update packages
RUN apt-get update -y && \
    apt-get upgrade -y

# Install MySQL
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server

# Copy configuration
COPY ./my.cnf /etc/mysql/my.cnf

# Expose MySQL port
EXPOSE 3306

# Run MySQL on container startup
CMD ["/usr/sbin/mysqld"]
