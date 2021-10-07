#web: uwsgi uwsgi.ini
#web: gunicorn -k gevent -w 2 socket_app:app
web: gunicorn --worker-class eventlet -w 3 socket_app:app
#web: gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 3 socket_app:app
