#! /usr/bin/env python
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS
import json
import time
from monitors import parse_ping, parse_http
from datetime import datetime
# initialize
app = Flask(__name__)
app.config["SECRET_KEY"] = "EbubeAsoSocket"
CORS(app)
socket = SocketIO(app)
ping_avg = [] # list for ping averages
http_list = [] # list of HTTP response times
# set up the main route
@app.route("/")
def index():
    return render_template("index.html")
def connected(methods=['GET', 'POST']):
    print("The client is now connected!")

def the_response(methods=['GET', 'POST']):
    print("Pierre the polecat")
# make the socketIO connection
@socket.on("connection")
def handle_connection(msg):
    #print("Connected!!")
    the_data = json.loads(msg)
    if the_data["Report"] == "Ping":
        avg = parse_ping(the_data["Server"])
        timestamp = datetime.now().strftime("%H:%M'%S")
        emit("Call", json.dumps({'Time': timestamp, 'TheData': avg}))
        time.sleep(the_data["TimeInterval"]/2) # The time interval to do the ping (seconds)
    if the_data["Report"] == "HTTP":
        res = parse_http(the_data["Server"], the_data["Port"])
        timestamp = datetime.now().strftime("%H:%M'%S")
        emit("Call", json.dumps({'Time': timestamp, 'TheData': res}))
        time.sleep(the_data["TimeInterval"]/2) # The time interval to do the HTTP requests (seconds)

# Run the socket server
if __name__ == "__main__":
    print("This websocket server is live and is listening")
    # socket.run(app)
    socket.run(app, host="0.0.0.0")
