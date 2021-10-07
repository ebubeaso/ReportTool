#web: uwsgi uwsgi.ini
web: gunicorn -k gevent -w 1 socket_app:app
