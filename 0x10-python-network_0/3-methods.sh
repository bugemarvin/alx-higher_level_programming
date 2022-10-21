#!/bin/bash
# Request method that accepts all the HTTP server URL requests
curl -sI -d PUT -X OPTIONS $1 -L
