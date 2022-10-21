#!/bin/bash
# Sends a POST request and displays the body of the response 'email' | value 'test@gmail.com' | subject 'I will always be here for PLD'
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" $2 $3 $4
