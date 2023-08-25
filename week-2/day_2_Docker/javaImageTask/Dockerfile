# Use a base image that has Maven and JDK
FROM maven:3.8.1-openjdk-11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the pom.xml file into the Docker image
COPY pom.xml /app

# Copy the source code into the Docker image
COPY src /app/src

# Build the project
RUN mvn package

# Add the entrypoint script into the Docker image
ADD entrypoint.sh /app/entrypoint.sh

# Give execute permission to the script
RUN chmod +x /app/entrypoint.sh

# Use the script as the entrypoint of the Docker image
ENTRYPOINT ["/app/entrypoint.sh"]

