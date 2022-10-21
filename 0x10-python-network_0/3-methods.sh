#!/bin/bash
# Request method that accepts all the HTTP server URL requests
curl -s --head $1 -L | grep "Allow:" | cut -d " " -f 2-4
