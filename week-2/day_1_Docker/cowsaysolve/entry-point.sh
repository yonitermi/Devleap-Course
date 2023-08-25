#!/bin/sh

# Export the port number
export PORT=${1:-8080}

# Change to the src directory where package.json is located
cd /usr/src/app/src

# Start the server
npm start


