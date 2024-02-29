#!/bin/bash
# script that sends a GET request to the URL with the header variable X-School-User-Id with the value 98
curl -sLH "X-School-User-Id: 98" "$1"
