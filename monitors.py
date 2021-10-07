#! /usr/bin/env python
from icmplib import ping
import requests
# This is a function for parsing ping requests
def parse_ping(server):
    result = ping(address=server, count=2, privileged=False)
    average = round((result.avg_rtt), 1)
    return average
# This is a function for parsing HTTP requests
def parse_http(server, port):
    # get the http response
    response = requests.get(f"http://{server}:{port}")
    # convert the elapsed time into milliseconds and round to one decimal place
    response_time = round(response.elapsed.total_seconds() * 1000, 1)
    return response_time
