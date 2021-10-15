#! /usr/bin/env python
import requests
import socket
import time
# This is a function for parsing ping requests
def parse_ping(server):
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
    start_time=time.time()
    if int(port) == 443:
        socket.getaddrinfo(server, port=443)
        https_sum = ( (time.time() - start_time) * 1000 )
        average = round( https_sum, 1 )
        return average
    socket.getaddrinfo(server, port=port)
    http_sum = ( (time.time() - start_time) * 1000 )
    response_time = round(http_sum, 1)
    return response_time
