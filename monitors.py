#! /usr/bin/env python
# from icmplib import ping
import requests
import socket
import time
# This is a function for parsing ping requests
def parse_ping(server):
    # result = ping(address=server, count=2, privileged=False)
    # average = round((result.avg_rtt), 1)
    ping_sum = 0
    start_time=time.time()
    for i in range(2):
        socket.getaddrinfo(server, port=None)
        ping_sum += ( (time.time() - start_time) * 1000 )
    average = round( (ping_sum//2),1 )
    return average
# This is a function for parsing HTTP requests
def parse_http(server, port):
    # get the http response
    response = requests.get(f"http://{server}:{port}")
    # convert the elapsed time into milliseconds and round to one decimal place
    response_time = round(response.elapsed.total_seconds() * 1000, 1)
    return response_time
