#!/bin/bash
# Request method that accepts all the HTTP server URL requests
curl -s --head -d PUT -x OPTIONS $1 -L | grep "Allow:" | cut -d " " -f 2-4
