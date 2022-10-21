#!/bin/bash
# sending a GET request with body response value 98
curl -sX GET $1 -L -H "X-School-User-Id: 98" $2 $3 $4
