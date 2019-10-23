from api import app
from gevent.pywsgi import  WSGIServer
from config import sslfile
import os



keyfilename = os.path.join(sslfile, 'ca.key')
certfilename = os.path.join(sslfile, 'mysite.crt')
print(keyfilename)
print(certfilename)
#
http_server = WSGIServer(('0.0.0.0', 5500), app, keyfile=keyfilename, certfile=certfilename)
http_server.serve_forever()
#,keyfile=keyfilename,certfile=certfilename