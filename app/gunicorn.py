import os

SERVER_PORT = os.getenv('SERVER_PORT', 5000)
bind = "0.0.0.0:{}".format(SERVER_PORT)


workers = 2
worker_connections = 512
worker_class = 'gevent'
timeout = 30
backlog = 512

daemon = False
pidfile = None
umask = 0
user = None
group = None

tmp_upload_dir = None
errorlog = '-'
loglevel = 'debug'
#accesslog = '-'
# access_log_format = '{"remote_ip":"%(h)s","request_id":"%({X-Request-Id}i)s","response_code":"%(s)s","request_method":"%(m)s","request_path":"%(U)s","request_querystring":"%(q)s","request_timetaken":"%(D)s","response_length":"%(B)s"}'
