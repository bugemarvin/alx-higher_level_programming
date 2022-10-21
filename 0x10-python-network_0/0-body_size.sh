#!/bin/bash
# script that takes in a URL, outputs the length.
curl -s --head $1 | grep "Content-Length:" | cut -d " " -f '2' 
