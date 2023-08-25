# Using a small Alpine-based Node.js image
FROM node:alpine

# Create app directory
WORKDIR /usr/src/app

# Change into the src directory where package.json is located
WORKDIR /usr/src/app/src

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
COPY src/package*.json ./

# Install all dependencies
RUN npm install

# Bundle app source
COPY src .

# Go back to the app directory
WORKDIR /usr/src/app

# Setting the environment variable for the port
ENV PORT=8080

# Copying the entry-point.sh
COPY entry-point.sh /
RUN chmod +x /entry-point.sh

# Expose the port
EXPOSE 3001

# Run the entry-point script
ENTRYPOINT ["/entry-point.sh"]

