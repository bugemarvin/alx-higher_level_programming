#!/bin/bash
# Request method that accepts all the HTTP server URL requests
curl -s --head 0.0.0.0:5000/route_4 -X OPTIONS | grep "Allow" | cut -d " " -f 2-4
