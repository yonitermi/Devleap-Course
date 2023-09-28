# Existing Jenkins setup
ARG JENKINS_IMAGE=docker.io/jenkins/jenkins
ARG JENKINS_TAG=lts
FROM "${JENKINS_IMAGE}:${JENKINS_TAG}"

# Install plugins
COPY plugins.txt plugins.txt
RUN jenkins-plugin-cli --plugin-file plugins.txt

# Switch to root to get permissions for installations
USER root

# Install Docker
RUN curl -fsSL https://get.docker.com | sh
RUN usermod -aG docker jenkins

# Set Host Docker GID
ARG HOST_DOCKER_GID
RUN groupmod -o -g "$HOST_DOCKER_GID" docker

# Switch back to Jenkins user
USER jenkins
