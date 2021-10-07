#web: uwsgi uwsgi.ini
web: gunicorn --worker-class eventlet -w 1 socket_app:app
