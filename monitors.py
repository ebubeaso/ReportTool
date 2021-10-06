#! /usr/bin/env python
import subprocess
import requests
# This is a function for parsing ping requests
def parse_ping(server):
    response_list = []
    total = 0
    average = 0
    # set the command to run
    command = ["ping", "-c", "2", server]
    # capture the standard output
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    # This returns a tuple of the standard out and standard error
    result = process.communicate()
    # I put "decode" here since the standard output is in a bytestring and I want it as a string
    stdout = result[0].decode("utf-8")
    """
    I use the .split() method to parse the string into an array by "time=", since that
    is where I would get the average response time of a ping packet.
    """
    if "time=" not in stdout:
        average = 0
        return average
    for i in stdout.split("time="):
        # Looks for " ms" since that will give us the response time
        if " ms" in i:
            response_time = i.split("\n")
            response_list.append(response_time[0])
    for res in response_list:
        # change each value in response_list into a float and add it to total
        number = float(res[:(res.index("ms") - 1)])
        total += number
    average = round((total / len(response_list)), 1)
    return average
# This is a function for parsing HTTP requests
def parse_http(server, port):
    # get the http response
    response = requests.get(f"http://{server}:{port}")
    # convert the elapsed time into milliseconds and round to one decimal place
    response_time = round(response.elapsed.total_seconds() * 1000, 1)
    return response_time
