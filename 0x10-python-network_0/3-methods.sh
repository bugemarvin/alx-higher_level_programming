#!/bin/bash
# Request method that accepts all the HTTP server URL requests
curl -sI $1 -L -X OPTIONS | grep "Allow:" | cut -d " " -f 2-
