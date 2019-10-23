import os,logging
os.environ["MXNET_CUDNN_AUTOTUNE_DEFAULT"] = '0'
os.environ['CUDA_VISIBLE_DEVICES']='6'
from app2 import app
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='logger.log', level=logging.INFO,format=LOG_FORMAT)


# http_server = HTTPServer(WSGIContainer(app),ssl_options={
#    "certfile": os.path.join(os.path.join("./server/"), "server.crt"),
#    "keyfile": os.path.join(os.path.join("./server/"), "server.key")})
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5502)
IOLoop.instance().start()
